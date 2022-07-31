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
THistAve = 1 # Plot histogram of average temps 

#######################################
# Create index for each file
#######################################
efnum = []
for i in range(0, len(enames)):
	for j in range(0, len(elblidx[i])):
		efnum.append(i)

Tnumf = len(elbl) # Number of filtered datasets 

#######################################
# Set up plotting parameters
#######################################
figi = 1 # Figure iterator
# figrootname = './Figures/' + datetime.now().strftime('%y%m%d') + '_' # Root file name for saving figures
figrootname = './Figures/' # Root file name for saving figures


# Get color options
[clrs, CUclrs] = daf.defcolors(Tnumf)

# Color and font settings for plots
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color = clrs) 
mpl.rcParams["figure.figsize"] = (12, 6.75)

#######################################
# Set up summary data frame and begin to fill
#######################################
edtstr = []
eleg = []

for i in range(0, Tnumf):
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

for i in range(0, Tnumf):
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

if TempProfiles == 1:
	# Plot all temperatures for each experiment in a separate window
	for i in range(0, Tnumf):
		plt.figure()
		figi += 1
		for j in range(0, len(Tagstr[i])):
			plt.plot(edata[i]['Time'], edata[i][Tagstr[i][j]])
		
		plt.legend(Tagstr[i])
		plt.title(edatestrs[efnum[i]] + ' ' + elbl[i])
		
		if TimeB4Air[i] > 0:
			plt.plot([AirTime[i], AirTime[i]], [0, Tmax[i]], 'k:')


#######################################
# Histogram
#######################################
if THistAve == 1:
	plt.figure(figi)
	figi += 1 
	ix = np.arange(0,Tnumf)

	# Create Legend
	plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$')
	plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$')
	plt.legend( ['No Ignition', 'Ignition'], loc='upper left')

	plt.bar(ix, Tsmry['AvePreheatTemp'], yerr=Tsmry['AvePreheatTempStd'], color=CUclrs[0])
	plt.xticks(ix, expID)
	plt.ylabel('Temperature [$^\circ$C]')
	plt.title('Average Preheat Temperatures')
	plt.ylim(0,400)
	tloc = Tsmry['AvePreheatTemp'] + Tsmry['AvePreheatTempStd']
	tloc = tloc* 1.01

		# Labels above bars
	for i in range(0, Tnumf):
		# Add labels to each bar with temperature value
		plt.text(ix[i], tloc[i], '%0.f' % Tsmry['AvePreheatTemp'][i], horizontalalignment='center')

	tloc = tloc + 10

	# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
	for i in range(0, Tnumf):
		if igstr[i] == 'Ignition':
			plt.text(ix[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size = 16)
		elif igstr[i] == 'No':
			plt.text(ix[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size = 16)
		elif igstr[i] == 'Ignition without Propegation':
			plt.text(ix[i], tloc[i], '\u26A1 ', c='r', horizontalalignment='center', size = 16)
			plt.text(ix[i], tloc[i], '\u2744', c='c', size = 16)
		else:
			plt.text(ix[i], tloc[i], '????', c='r', horizontalalignment='center', size = 16)

	plt.savefig(figrootname + 'IgnitionTemps.png')

#######################################
# Output temperature data to csv
#######################################
Tofname = __file__
Tofname = Tofname[:-3]
Tofname = Tofname + 'Temp_Experiment_Summary.csv'
Tsmry.to_csv(Tofname)

#######################################
# Show plots!
#######################################
plt.show()