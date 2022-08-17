# Import Libraries
import DAF2 as daf
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

#######################################
# Import Benchmark and Experimental Data File information
#######################################
from HeaderExperimentData import *

#######################################
# Global Variables
#######################################
TempProfiles = 0 # Plot temp profiles for each experiment in a new window
TCprofiles = 1 # Plot temp profiles for all experiments for each TC in a separate window
AvePHTemp = 0 # Plot histogram of average temps 
PreheatTime = 0 # Plot preheat time in minutes for each experiment
MaxTemps = 0 # Plot max temperatures for each experiment

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
mpl.rcParams["figure.figsize"] = (12, 6.75)

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

#######################################
# Read and filter data for time while sunlight is being collected
#######################################
Tagstr = []
Tmax = []
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
	
	#  Create temperature tag strings
	Tagstr.append([])
	dc = datai.columns
	for j in range(0, len(dc)):
		if 'Temp' in dc[j]:
			Tagstr[i].append(dc[j]) 

	# Filter data
	dataif = daf.data_filter(datai, edatestrs[efnum[i]], Tempi[i], Tempf[i])

	# If aeration was not initiated
	if AirT[i] == 'X':
		TimeB4Air.append(0)
		AirTime.append(0)
	else:
		Atime = datetime.strptime(edatestrs[efnum[i]] + ' ' + AirT[i], '%y%m%d %H:%M:%S')
		Adt = (Atime - dataif['Time'][dataif.index.min()]).total_seconds()/60
		AirTime.append(Atime)
		TimeB4Air.append(Adt)

	# Calculate max temp
	TempMaxes = dataif[Tagstr[i]].max()
	Tmaxoverall = TempMaxes.max()
	Tmax.append(Tmaxoverall)

	Tfilt = (dataif['Time'] <= Atime) & (dataif['Time'] <= (Atime - timedelta(minutes = 1))) 
	dataf = dataif.loc[Tfilt]
	
	PHT1.append(dataif['Temp3'].mean())
	PHT2.append(dataif['Temp4'].mean())
	PHT3.append(dataif['Temp6'].mean())
	PHT1stdv.append(dataif['Temp3'].std())
	PHT2stdv.append(dataif['Temp4'].std())
	PHT3stdv.append(dataif['Temp6'].std())
	AvePHT.append(np.mean([dataif['Temp3'].mean(), dataif['Temp4'].mean(), dataif['Temp6'].mean()]))
	AvePHTstd.append(np.std([dataif['Temp3'].mean(), dataif['Temp4'].mean(), dataif['Temp6'].mean()]))


	edata.append(dataif)

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


#######################################
# Plot temperature profiles for each experiment in a separte window
#######################################
if TempProfiles == 1:
	# Plot all temperatures for each experiment in a separate window
	for i in range(0, enumf):
		plt.figure()
		figi += 1
		for j in range(0, len(Tagstr[i])):
			plt.plot(edata[i]['Time'], edata[i][Tagstr[i][j]])
		
		plt.legend(Tagstr[i])
		
		if figtitles == 1:
			plt.title(edatestrs[efnum[i]] + ' ' + elbl[i])
		
		if TimeB4Air[i] > 0:
			plt.plot([AirTime[i], AirTime[i]], [0, Tmax[i]], 'k:')

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
		elif igstr[i] == 'Ignition without Propegation':
			sym = '\u26A1 ' + '\u2744'
		else:
			sym = '????'

		expleg.append(expID[i] + ' ' + sym) 

	for i in range(0, len(Tagstr[0])):
		plt.figure()
		figi += 1
		
		plt.subplot(312)
		for j in range(0, enumf):
			if igstr[j] == 'Ignition':
				print(igstr[j])
				plt.plot(edata[j]['RunTime'], edata[j][Tagstr[0][i]], c=clrs[j])
			
		plt.xlabel('Run Time [mins]')
		plt.ylabel('Temperature $^o$C')
		plt.title('Comparison of Profiles for ' + Tagstr[0][i] + ' which Achieved Ignition')

		plt.subplot(313)
		for j in range(0, enumf):
			if igstr[j] != 'Ignition':
				
				plt.plot(edata[j]['RunTime'], edata[j][Tagstr[0][i]], c=clrs[j])
			
		plt.xlabel('Run Time [mins]')
		plt.ylabel('Temperature $^o$C')
		plt.title('Comparison of Profiles for ' + Tagstr[0][i] + ' which Didn\'t Ignite')

		plt.subplot(311)
		for j in range(0, enumf):
			plt.plot(edata[j]['RunTime'], edata[j][Tagstr[0][i]])
			

		plt.xlabel('Run Time [mins]')
		plt.ylabel('Temperature $^o$C')
		plt.title('Comparison of Profiles for ' + Tagstr[0][i])
		
		plt.legend(expleg)

		

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
			plt.bar(bar_loc[i], Tsmry['AvePreheatTemp'][i], yerr=Tsmry['AvePreheatTempStd'][i], color=CUclrs[1])
		else:
			plt.bar(bar_loc[i], Tsmry['AvePreheatTemp'][i], yerr=Tsmry['AvePreheatTempStd'][i], color=CUclrs[0])
	
	plt.xticks(bar_loc, expID)
	plt.ylabel('Temperature [$^\circ$C]')
	plt.ylim(0,400)
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
			plt.text(bar_loc[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size = 16)
		elif igstr[i] == 'No':
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size = 16)
		elif igstr[i] == 'Ignition without Propegation':
			plt.text(bar_loc[i], tloc[i], '\u26A1 ', c='r', horizontalalignment='center', size = 16)
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', size = 16)
		else:
			plt.text(bar_loc[i], tloc[i], '????', c='r', horizontalalignment='center', size = 16)

	plt.savefig(figrootname + 'PreheatTemps.png')

#######################################
# Average Preheat Times
#######################################
if PreheatTime == 1:
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

	for i in range(0, enumf):
		if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
			plt.bar(bar_loc[i], Tsmry['PreheatTime'][i], color=CUclrs[1])
		else:
			plt.bar(bar_loc[i], Tsmry['PreheatTime'][i], color=CUclrs[0])
	
	# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
	for i in range(0, enumf):
		tloc = Tsmry['PreheatTime'][i] + 2

		plt.text(bar_loc[i], tloc, '%0.f' % Tsmry['PreheatTime'][i], horizontalalignment='center')

		tloc = tloc + 8

		if igstr[i] == 'Ignition':
			plt.text(bar_loc[i], tloc, '\u26A1', c='r', horizontalalignment='center', size = 16)
		elif igstr[i] == 'No':
			plt.text(bar_loc[i], tloc, '\u2744', c='c', horizontalalignment='center', size = 16)
		elif igstr[i] == 'Ignition without Propegation':
			plt.text(bar_loc[i], tloc, '\u26A1 ', c='r', horizontalalignment='center', size = 16)
			plt.text(bar_loc[i], tloc, '\u2744', c='c', size = 16)
		else:
			plt.text(bar_loc[i], tloc, '????', c='r', horizontalalignment='center', size = 16)

	
	plt.xlabel('Experiment ID')
	plt.xticks(bar_loc, expID)
	plt.ylabel('Preheat Time [mins]')
	plt.ylim(0, 325)

	if figtitles == 1:
		plt.title('Time Heated Before Aeration')

	plt.savefig(figrootname + 'PreheatTimes.png')

#######################################
# Max Temps Preheat Times
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
	plt.ylim(0,1500)
	plt.xlabel('Experiment ID')

	if figtitles == 1:
		plt.title('Maximum Measured Temperature for Each Experiment')
	
	tloc = Tsmry['T_Max'] + 15

	for i in range(0, enumf):
		plt.text(bar_loc[i], tloc[i], '%0.f' % Tsmry['T_Max'][i], horizontalalignment='center')

	tloc = tloc + 35

	for i in range(0, enumf):
		if igstr[i] == 'Ignition':
			plt.text(bar_loc[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size = 16)
		elif igstr[i] == 'No':
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size = 16)
		elif igstr[i] == 'Ignition without Propegation':
			plt.text(bar_loc[i], tloc[i], '\u26A1 ', c='r', horizontalalignment='center', size = 16)
			plt.text(bar_loc[i], tloc[i], '\u2744', c='c', size = 16)
		else:
			plt.text(bar_loc[i], tloc[i], '????', c='r', horizontalalignment='center', size = 16)

	plt.savefig(figrootname + 'MaxTemps.png')


#######################################
# Output temperature data to csv
#######################################
Tofname = __file__
Tofname = Tofname[:-3]
Tofname = Tofname + '_Temp_Experiment.csv'
Tsmry.to_csv(Tofname)

#######################################
# Show plots!
#######################################
plt.show()