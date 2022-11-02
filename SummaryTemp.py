# Import Libraries
import DAF2 as daf
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np
import pysine
import time

#######################################
# Import Benchmark and Experimental Data File information
#######################################
from HeaderExperimentData import *

#######################################
# Global Variables
#######################################
TempProfiles = 0 # Plot temp profiles for each experiment in a new window
TCprofiles = 0 # Plot temp profiles for all experiments for each TC in a separate window
AvePHTemp = 1 # Plot histogram of average temps 
PreheatTimeFilter = 1 # Plot preheat time in minutes for each experiment
MaxTemps = 1 # Plot max temperatures for each experiment
AveMaxTemps = 1 # Plot the average of max temps from all TCs
PHFiltered = 0 # Plot filtered preheat data for each TC in separate subplot
HiRez = 0 # Plot High resolution temperature profiles


#######################################
# Create index for each file
#######################################
efnum = []
for i in range(0, len(enames)):
	for j in range(0, len(elblidx[i])):
		efnum.append(i)

enumf = len(elbl) # Number of filtered datasets 

#######################################
# Set up plotting parameters
#######################################
figi = 1 # Figure iterator
figrootname = './Figures/' # Root file name for saving figures
figtitles = 1 # Include figure titles
plt.style.use('./FigStyle.mplstyle') # Load figure settings from style file

# Get color options
[clrs, CUclrs] = daf.defcolors(enumf)

# Color and font settings for plots
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color = clrs) 
# mpl.rcParams["figure.figsize"] = (12, 6.75)

#######################################
# Set up summary data frame and begin to fill
#######################################
edtstr = []
eleg = []

for i in range(0, enumf):
	edtstr.append(edatestrs[efnum[i]])
	eleg.append(edatestrs[efnum[i]] + ' ' + elbl[i])

Tsmry =  pd.DataFrame()
Tsmry = Tsmry.assign(Date=edtstr)
Tsmry = Tsmry.assign(Name=eleg)

# Initiate variables
edata = []
PHdata = [] # Preheat data

#######################################
# Read and filter data for time while sunlight is being collected
#######################################
Tagstr = []
Tmax = []
Tmaxave = []
Tmaxstd = []
AirTime = []
TimeB4Air =[]

PHT1 = []
PHT2 = []
PHT3 = []
PHT1stdv = []
PHT2stdv = []
PHT3stdv = []
AvePHT = []
AvePHTstd = []

for i in range(0, enumf):
	# Read and format data
	datai = daf.data_read_format(efpath + enames[efnum[i]], edatestrs[efnum[i]])
	
	# Filter out disconnections
	datai = datai.replace(-9999, None) 

	if edatestrs[efnum[i]] == '220708':
		for j in range(1, 8):
			headstr = 'Temp' + str(j)
			datai[datai[headstr] > 850] = None

	if edatestrs[efnum[i]] == '220804':
		datai[datai['Temp1'] > 600] = None
	
	#  Create temperature tag strings
	Tagstr.append([])
	dc = datai.columns
	for j in range(0, len(dc)):
		if 'Temp' in dc[j]:
			Tagstr[i].append(dc[j]) 

	# Filter data
	if Tempi[i] == 0:
		ti = etistr[i]
	else: 
		ti = Tempi[i]

	if Tempf[i] == 0:
		tf = datai['Time'][datai.index.max()].strftime('%H:%M:%S')
	else:
		tf = Tempf[i]

	dataif = daf.data_filter(datai, edatestrs[efnum[i]], ti, tf)

	# If aeration was not initiated
	if AirT[i] == 'X':
		TimeB4Air.append(0)
		AirTime.append(0)
		tstart = datetime.strptime(edatestrs[efnum[i]] + ' ' +  ti, '%y%m%d %H:%M:%S')
		Atime = datetime.strptime(edatestrs[efnum[i]] + ' ' + tf, '%y%m%d %H:%M:%S')
	else:
		Atime = datetime.strptime(edatestrs[efnum[i]] + ' ' + AirT[i], '%y%m%d %H:%M:%S')
		tstart = datetime.strptime(edatestrs[efnum[i]] + ' ' +  ti, '%y%m%d %H:%M:%S')
		AirTime.append(Atime)
		Adt = (Atime - tstart).total_seconds()/60
		TimeB4Air.append(Adt)

	# Calculate max temp and average of max temps for all TCs
	TempMaxes = dataif[Tagstr[i]].max()
	Tmaxoverall = TempMaxes.max()
	Tmax.append(Tmaxoverall)
	Tmaxave.append(np.mean(TempMaxes))
	Tmaxstd.append(np.std(TempMaxes))

	# Calculate average temperatures for 1 minute before aeration started
	Tfilt = (dataif['Time'] <= Atime) & (dataif['Time'] >= (Atime - timedelta(minutes = 10))) 
	dataf = dataif.loc[Tfilt]
	
	print(dataf['Time'][dataf.index.min()])
	dRT = (dataf['Time'] - dataf['Time'][dataf.index.min()]).dt.total_seconds()
	dataf = dataf.assign(RunTime = dRT)
	# dataf['RunTime'] = (dataf['Time'] - dataf['Time'][dataf.index.min()]).dt.total_seconds()
	
	# In High Res TC case:
	if 'High Re' in elbl[i]:
		PHT1.append(dataf['Temp1'].mean())
		PHT2.append(dataf['Temp8'].mean())
		PHT3.append(dataf['Temp15'].mean())
		PHT1stdv.append(dataf['Temp1'].std())
		PHT2stdv.append(dataf['Temp8'].std())
		PHT3stdv.append(dataf['Temp15'].std())
		AvePHT.append(np.mean([dataf['Temp1'].mean(), dataf['Temp8'].mean(), dataf['Temp15'].mean(), dataf['Temp26'].mean(), dataf['Temp27'].mean()]))
		AvePHTstd.append(np.std([dataf['Temp1'].mean(), dataf['Temp8'].mean(), dataf['Temp15'].mean(), dataf['Temp26'].mean(), dataf['Temp27'].mean()]))
	
	# In all other cases
	else:
		PHT1.append(dataf['Temp3'].mean())
		PHT2.append(dataf['Temp4'].mean())
		PHT3.append(dataf['Temp6'].mean())
		PHT1stdv.append(dataf['Temp3'].std())
		PHT2stdv.append(dataf['Temp4'].std())
		PHT3stdv.append(dataf['Temp6'].std())
		AvePHT.append(np.mean([dataf['Temp3'].mean(), dataf['Temp4'].mean(), dataf['Temp6'].mean()]))
		AvePHTstd.append(np.std([dataf['Temp3'].mean(), dataf['Temp4'].mean(), dataf['Temp6'].mean()]))

	edata.append(dataif)

	PHdata.append(dataf)


# Output summary data to dataframe 
Tsmry = Tsmry.assign(PreheatT1=PHT1) # Prehat temperature 1
Tsmry = Tsmry.assign(PreheatT2=PHT2) # Prehat temperature 2
Tsmry = Tsmry.assign(PreheatT3=PHT3) # Prehat temperature 3
Tsmry = Tsmry.assign(PreheatT1std=PHT1stdv) # Prehat temperature 1
Tsmry = Tsmry.assign(PreheatT2std=PHT2stdv) # Prehat temperature 2
Tsmry = Tsmry.assign(PreheatT3std=PHT3stdv) # Prehat temperature 3
Tsmry = Tsmry.assign(AvePreheatTemp=AvePHT)
Tsmry = Tsmry.assign(AvePreheatTempStd=AvePHTstd)
Tsmry = Tsmry.assign(PreheatTime=TimeB4Air) # Prehat temperature 3
Tsmry = Tsmry.assign(T_Max=Tmax) # Power Estimates based on Flat Efficiency Value
Tsmry = Tsmry.assign(Tmax_ave = Tmaxave) # Average of maxes from all TCs
Tsmry = Tsmry.assign(Tmax_std = Tmaxstd) # Standard deviation of maxes for all TCs


#######################################
# Plot temperature profiles for each experiment in a separte window
#######################################
if TempProfiles == 1:
	# Plot all temperatures for each experiment in a separate window
	for i in range(0, enumf):
		plt.figure()
		figi += 1
		for j in range(0, len(Tagstr[i])):
			plt.plot(edata[i]['RunTime'], edata[i][Tagstr[i][j]])
		
		plt.legend(Tagstr[i])
		
		if figtitles == 1:
			plt.title(edatestrs[efnum[i]] + ' ' + elbl[i])
		
		if TimeB4Air[i] > 0:
			# plt.plot([AirTime[i], AirTime[i]], [0, Tmax[i]], 'k:')
			plt.plot([Tsmry['PreheatTime'][i], Tsmry['PreheatTime'][i]], [0, Tmax[i]], 'k:')
			

#######################################
# Plot temperature profiles for preheat thermocouples in preheat filter window
#######################################
if PHFiltered == 1:

	plt.figure()
	figi += 1
	
	plt.subplot(221)
	for j in range(0, enumf):
		plt.plot(PHdata[j]['RunTime'], PHdata[j]['Temp1'], c=clrs[j])
	plt.xlabel('Run Time [sec]')
	plt.ylabel('Temperature $^o$C')
	plt.title('Temp1 Preheat')

	plt.subplot(222)
	for j in range(0, enumf):
		plt.plot(PHdata[j]['RunTime'], PHdata[j]['Temp2'], c=clrs[j])
	plt.legend(expID)

	plt.ylabel('Temperature $^o$C')
	plt.title('Temp2 Preheat Filtered DAta')

	plt.subplot(223)
	for j in range(0, enumf):
		plt.plot(PHdata[j]['RunTime'], PHdata[j]['Temp3'], c=clrs[j])
		
	plt.xlabel('Run Time [sec]')
	plt.ylabel('Temperature $^o$C')
	plt.title('Temp 3 Preheat')


#######################################
# Plot temperature profiles for each thermocouple in a separte window
#######################################
if TCprofiles == 1:
	expleg = []
	for i in range(0, enumf):
		sym = []
		if igstr[i] == 'Ignition':
			sym = '\u26A1'
		elif igstr[i] == 'No':
			sym = '\u2744'
		elif igstr[i] == 'Ignition without Propagation':
			sym = '\u26A1 ' + '\u2744'
		else:
			sym = '????'

		expleg.append(expID[i] + ' ' + sym) 

	for i in range(0, len(Tagstr[0])):
		plt.figure()
		figi += 1
		
		plt.subplot(222)
		for j in range(0, enumf):
			if igstr[j] == 'Ignition':
				plt.plot(edata[j]['RunTime'], edata[j][Tagstr[0][i]], c=clrs[j])

		plt.ylabel('Temperature $^o$C')
		plt.title('Ignition with Propagation')

		plt.subplot(223)
		for j in range(0, enumf):
			if igstr[j] == 'No':
				plt.plot(edata[j]['RunTime'], edata[j][Tagstr[0][i]], c=clrs[j])
			
		plt.xlabel('Run Time [mins]')
		plt.ylabel('Temperature $^o$C')
		plt.title('No Ignition')

		plt.subplot(224)
		for j in range(0, enumf):
			if igstr[j] == 'Ignition without Propagation':
				plt.plot(edata[j]['RunTime'], edata[j][Tagstr[0][i]], c=clrs[j])
		
		plt.xlabel('Run Time [mins]')
		plt.ylabel('Temperature $^o$C')
		plt.title('Ignition without Propagation')

		plt.subplot(221)
		for j in range(0, enumf):
			plt.plot(edata[j]['RunTime'], edata[j][Tagstr[0][i]])
			
		plt.ylabel('Temperature $^o$C')
		plt.title('All Experiments')

		plt.legend(expleg)

		plt.suptitle('Comparison of Temperature Measurements Across Experiments for ' + Tagstr[0][i])


#######################################
# Average Preheat Temperature
#######################################
if AvePHTemp == 1:
	# Create figure
	plt.figure(figi)
	figi += 1 

	# Bar locaitons
	bar_loc = np.arange(0,enumf)

	# Create Legend
	plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$')
	plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$')
	plt.bar(0, 0, color=CUclrs[0])
	plt.bar(0, 0, color=CUclrs[1])
	plt.legend( ['No Ignition', 'Ignition', 'GAC', 'Petroleum'], loc='upper left')

	# Create bars
	for i in range(0, enumf):
		if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
			plt.bar(bar_loc[i], Tsmry['AvePreheatTemp'][i], yerr=Tsmry['AvePreheatTempStd'][i], capsize=4, color=CUclrs[1])
		else:
			plt.bar(bar_loc[i], Tsmry['AvePreheatTemp'][i], yerr=Tsmry['AvePreheatTempStd'][i], capsize=4, color=CUclrs[0])
	
	plt.xticks(bar_loc, expID)
	plt.ylabel('Temperature [$^\circ$C]')
	plt.xlabel('Experiment ID')

	if figtitles == 1:
		plt.title('Average Preheat Temperatures')

	tloc = Tsmry['AvePreheatTemp'] + Tsmry['AvePreheatTempStd']
	tloc = tloc* 1.01

		# Labels above bars
	for i in range(0, enumf):
		# Add labels to each bar with temperature value
		plt.text(bar_loc[i], tloc[i], '%0.f' % Tsmry['AvePreheatTemp'][i], horizontalalignment='center')

	tloc = tloc + 10

	# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
	for i in range(0, enumf):
		if igstr[i] == 'Ignition':
			plt.text(bar_loc[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size=16)
		elif igstr[i] == 'No':
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size=16)
		elif igstr[i] == 'Ignition without Propagation':
			plt.text(bar_loc[i], tloc[i], '\u26A1 ', c='r', horizontalalignment='center', size=16)
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', size=16)
		else:
			plt.text(bar_loc[i], tloc[i], '????', c='r', horizontalalignment='center', size=16)

	plt.ylim(0, tloc.max()+25)
	plt.savefig(figrootname + 'PreheatTemps.png')

#######################################
# Average Preheat Times
#######################################
if PreheatTimeFilter == 1:
	# Create figure
	plt.figure(figi)
	figi += 1 

	# Bar locaitons
	bar_loc = np.arange(0,enumf)

	# Create Legend
	plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$')
	plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$')
	plt.bar(0, 0, color=CUclrs[0])
	plt.bar(0, 0, color=CUclrs[1])
	plt.legend( ['No Ignition', 'Ignition', 'GAC', 'Petroleum'], loc='upper left')

	PowData = pd.read_csv('SummaryPower_Experiment.csv', header = 0)

	tloc = []
	for i in range(0, enumf):
		
		if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
			plt.bar(bar_loc[i], Tsmry['PreheatTime'][i], color=CUclrs[1], yerr=PowData['PoutTotalEST_STD_TL'][i], capsize=4)
			tloc.append(Tsmry['PreheatTime'][i] + PowData['PoutTotalEST_STD_TL'][i])
		elif Tsmry['PreheatTime'][i] == 0:
			plt.bar(bar_loc[i], Tsmry['PreheatTime'][i], color=CUclrs[0])
			tloc.append(Tsmry['PreheatTime'][i])
		else:
			plt.bar(bar_loc[i], Tsmry['PreheatTime'][i], color=CUclrs[0], yerr=PowData['PoutTotalEST_STD_TL'][i], capsize=4)
			tloc.append(Tsmry['PreheatTime'][i] + PowData['PoutTotalEST_STD_TL'][i])
	
	# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
	for i in range(0, enumf):
		
		tloc[i] = tloc[i] + 2

		plt.text(bar_loc[i], tloc[i], '%0.f' % Tsmry['PreheatTime'][i], horizontalalignment='center')

		tloc[i] = tloc[i] + 8

		if igstr[i] == 'Ignition':
			plt.text(bar_loc[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size=16)
		elif igstr[i] == 'No':
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size=16)
		elif igstr[i] == 'Ignition without Propagation':
			plt.text(bar_loc[i], tloc[i], '\u26A1 ', c='r', horizontalalignment='center', size=16)
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', size=16)
		else:
			plt.text(bar_loc[i], tloc[i], '????', c='r', horizontalalignment='center', size=16)

	plt.text(bar_loc[15], 250, 'Error bars represent variability in power')
	plt.xlabel('Experiment ID')
	plt.xticks(bar_loc, expID)
	plt.ylabel('Preheat Time [mins]')
	plt.ylim(0, max(tloc) + 20)

	if figtitles == 1:
		plt.title('Time Heated Before Aeration')

	plt.savefig(figrootname + 'PreheatTimes.png')

#######################################
# Max Temps
#######################################
if MaxTemps == 1:
	# Create figure
	plt.figure(figi)
	figi += 1 

	# Bar locaitons
	bar_loc = np.arange(0,enumf)

	# Create Legend
	plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$')
	plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$')
	plt.bar(0, 0, color=CUclrs[0])
	plt.bar(0, 0, color=CUclrs[1])
	plt.legend( ['No Ignition', 'Ignition', 'GAC', 'Petroleum'], loc='upper left')

	# Create bars
	for i in range(0, enumf):
		if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
			plt.bar(bar_loc[i], Tsmry['T_Max'][i], color=CUclrs[1])
		else:
			plt.bar(bar_loc[i], Tsmry['T_Max'][i], color=CUclrs[0])

	plt.xticks(bar_loc, expID)
	plt.ylabel('Temperature [$^\circ$C]')
	plt.ylim(0,1150)
	plt.xlabel('Experiment ID')

	if figtitles == 1:
		plt.title('Maximum Measured Temperature for Each Experiment')
	
	tloc = Tsmry['T_Max'] + 15

	for i in range(0, enumf):
		plt.text(bar_loc[i], tloc[i], '%0.f' % Tsmry['T_Max'][i], horizontalalignment='center')

	tloc = tloc + 35

	for i in range(0, enumf):
		if igstr[i] == 'Ignition':
			plt.text(bar_loc[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size=16)
		elif igstr[i] == 'No':
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size=16)
		elif igstr[i] == 'Ignition without Propagation':
			plt.text(bar_loc[i], tloc[i], '\u26A1 ', c='r', horizontalalignment='center', size=16)
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', size=16)
		else:
			plt.text(bar_loc[i], tloc[i], '????', c='r', horizontalalignment='center', size=16)

	plt.savefig(figrootname + 'MaxTemps.png')

#######################################
# Average of Max Temps
#######################################
if AveMaxTemps == 1:
	# Create figure
	plt.figure(figi)
	figi += 1 

	# Bar locaitons
	bar_loc = np.arange(0,enumf)

	# Create Legend
	plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$')
	plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$')
	plt.bar(0, 0, color=CUclrs[0])
	plt.bar(0, 0, color=CUclrs[1])
	plt.legend( ['No Ignition', 'Ignition', 'GAC', 'Petroleum'], loc='upper left')

	# Create bars
	for i in range(0, enumf):
		if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
			plt.bar(bar_loc[i], Tsmry['Tmax_ave'][i], color=CUclrs[1], yerr=Tsmry['Tmax_std'][i], capsize=4)
		else:
			plt.bar(bar_loc[i], Tsmry['Tmax_ave'][i], color=CUclrs[0], yerr=Tsmry['Tmax_std'][i], capsize=4)

	plt.xticks(bar_loc, expID)
	plt.ylabel('Temperature [$^\circ$C]')
	plt.ylim(0,1150)
	plt.xlabel('Experiment ID')

	if figtitles == 1:
		plt.title('Average of Maximum Measured Temperature among Thermocouples')
	
	tloc = Tsmry['Tmax_ave'] + Tsmry['Tmax_std'] + 15

	for i in range(0, enumf):
		plt.text(bar_loc[i], tloc[i], '%0.f' % Tsmry['Tmax_ave'][i], horizontalalignment='center')

	tloc = tloc + 35

	for i in range(0, enumf):
		if igstr[i] == 'Ignition':
			plt.text(bar_loc[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size=16)
		elif igstr[i] == 'No':
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size=16)
		elif igstr[i] == 'Ignition without Propagation':
			plt.text(bar_loc[i], tloc[i], '\u26A1 ', c='r', horizontalalignment='center', size=16)
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', size=16)
		else:
			plt.text(bar_loc[i], tloc[i], '????', c='r', horizontalalignment='center', size=16)

	plt.savefig(figrootname + 'AveMaxTemps.png')

#######################################
# High Rez Temp Profiles 
#######################################
if HiRez == 1:
	
	# Collect data indices for high resolution experiments
	HR_i = [] # High Resolution indices
	for i in range(0, enumf):
		if 'High Re' in elbl[i]:
			HR_i.append(i)


	for i in HR_i:
		# Set up new ifgur 
		plt.figure(figi)
		figi += 1

		plt.suptitle(edatestrs[efnum[i]] + elbl[i])

		plt.subplot(411)
		plt.title('Center Column of TCs')
		plt.subplot(412)
		plt.title('Left Column')
		plt.subplot(413)
		plt.title('Right Column')
		plt.subplot(414)
		plt.title('Bottom TCs')
		plt.xlabel('Run Time [mins]')

		for j in range(0, len(Tagstr[i])):

			if j < 7:
				plt.subplot(411)
				plt.plot(edata[i]['RunTime'], edata[i][Tagstr[i][j]], c=clrs[j])
			elif j <14:
				plt.subplot(412)
				plt.plot(edata[i]['RunTime'], edata[i][Tagstr[i][j]], c=clrs[j-7])
			elif j < 21:
				plt.subplot(413)
				plt.plot(edata[i]['RunTime'], edata[i][Tagstr[i][j]], c=clrs[j-14])
			
			plt.legend(['0 cm from bottom', '1 cm', '2.5 cm', '5 cm', '7.5 cm', '10 cm', '12.5 cm'])

		legstr = [] # legend strings
		for k in [0, 7, 14, 25, 16]:
			plt.subplot(414)
			plt.plot(edata[i]['RunTime'], edata[i][Tagstr[i][k]], c=clrs[7+k])
			legstr.append(Tagstr[i][k])
		plt.legend(legstr)





#######################################
# Output temperature data to csv
#######################################
Tofname = __file__
Tofname = Tofname[:-3]
Tofname = Tofname + '_Temp_Experiment.csv'
Tsmry.to_csv(Tofname)

#######################################
# Play tone to signify end of script
#######################################
pysine.sine(frequency=440.0, duration=0.25)
time.sleep(0.1)
pysine.sine(frequency=440.0, duration=0.1)
time.sleep(0.1)
pysine.sine(frequency=440.0, duration=0.1)
pysine.sine(frequency=880.0, duration=1)


#######################################
# Show plots!
#######################################
plt.show()