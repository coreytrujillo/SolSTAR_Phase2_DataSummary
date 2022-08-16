#!/usr/bin/env python

# Import Libraries
import DAF2 as daf
from datetime import datetime
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

#######################################
#  Comment Legend
#######################################
# BM = benchmark
# CF = Collector/Fiber
# FA = Flat Average (efficiency)
# @ = important

#######################################
# Plot Toggles
#######################################

# Benchmark data
BM = 1 # Benchmark Data
if BM == 1:
	TimePout = 0 # Power output over time
	TimePin = 0 # Power input over time
	PinPout = 1 # @ Power in vs power out for all benchmarks
	AvePinPout = 0 # Average Power in vs. Power out
	PinEff = 1 # @ Power In vs. Efficiency
	AvePinEff = 0 # Average power in vs. Efficiency
	EffPout = 0 # Efficiency vs. Power out
	AveEffPout = 0 # Average Efficiency vs. Power out

# Benchmark data filtered for data of interest
SubSet = 1 # Plot a select subset of data (particular collector fiber pairs)
if SubSet == 1:
	CFEff = 1 # @ Bar plot efficiencies for select collector/fiber pairs
	SSPinPout = 1 # @ Plot Power in vs. Power out for subset data on a single plot
	SSPinPoutSubplot = 1 # @ Plot Power In vs Power Out for each collector/fiber pair on its own subplot
	SSPinEff = 0 # Subset: Power In vs. Efficiency in separte subplots
	SSPowOutEff = 0 # Subset: Efficiency vs. Power Out in separate subplots
	SSAvePowInPowOut = 0 # Subset: Average Power In vs. Power Out


ExpData = 1 # Plot experimental data
if ExpData == 1:
	ExpShowFilters = 0 # Filter experimental data for time sunlight is collected
	ExpPinBar = 1 # @ Plot power input for each experiment
	PinPoutTLs = 1 # @ Plot benchmark Pin vs Pout with trendlines
	PinPoutTLs_WithPyHi = 1 # @ Plot benchmark Pin vs Pout with high irradiance data overlayed
	PyHiPinPoutTLs = 1 # @ Plot benchmark Pin vs Pout filtered for high irradiance with TLs
	AvePinPoutTLs = 1 # Plot average benchmark data and experimental data with trendlines
	CFPinPout = 1 # Plot aveage power in vs. Power out
	PoutHist = 1 # Plot a histogram of total power for each experiment
	PoutHistCombined = 1 # Histogram of combined power output for each experiment 

############################################################################################
# Do not edit below this line
############################################################################################

#######################################
# Import Benchmark and Experimental Data File information
#######################################
from HeaderBenchmarkData import *
from HeaderExperimentData import *

#######################################
# Define commonly used variables
#######################################
Ac = pi*0.6**2/4 - pi*0.1**2/4 # Area of the collector minus area of quartz rod housing
print('Collector Area', '%0.3f' % Ac, 'm2')

#######################################
# Set up plotting parameters
#######################################
# Get color options
[clrs, CUclrs] = daf.defcolors(len(BMlbl))

# Figure settings
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color = clrs)  # Define color cycle
plt.style.use('./FigStyle.mplstyle') # Load figure settings from style file
figrootname = './Figures/' # Figure Output name root | optional: datetime.now().strftime('%y%m%d')
figi = 1 # Initiate igure iterator
figtitles = 1 # Include titles on figures?

############################################################################################
############################################################################################
############################################################################################
# Benchmark Data
############################################################################################
############################################################################################
############################################################################################


############################################################################################
# Read benchmark data,  filter, and summarize
############################################################################################

#######################################
# Create index to correlate each experiment to its file
#######################################
BMfnum = [] # File number associated with each experiment
BMnumf = len(BMlbl) # Number of filtered datasets for benchmarks
for i in range(0, len(BMfnames)):
	for j in range(0, len(lblidx[i])):
		BMfnum.append(i)

#######################################
# Read and filter Benchmark data and compile in single variable
#######################################

# Variables to compile all Benchmark data
BMdata = [] # Variable containing all benchmark DataFrames
PoutAve = [] # Average Power output for each experiment
PoutStd = [] # Power output standard deviaiton 
PinAve = [] # Average power input 
PinStd = [] # Power input standard deviatoin
PyrAve = [] # Average Irradiance
PyrStd = [] # Irradiance standard deviation
EffAve = [] # Average efficiency
EffStd = [] # Efficiency standard deviation

for i in range(0, BMnumf):
	# Read and format data 
	datai = daf.data_read_format(fpath + BMfnames[BMfnum[i]], BMdatestrs[BMfnum[i]])
	if (BMdatestrs[BMfnum[i]] == '220313') or (BMdatestrs[BMfnum[i]] == '220314') or (BMdatestrs[BMfnum[i]] == '220315'):
		datai['PyrE'] = -datai['PyrE']
	
	# Change dataframe header name for power output
	datai = datai.rename(columns={'Power':'Pout'})

	#  Calculate Power input  and create a column for it in the dataframe
	datai = datai.assign(Pin=datai['PyrE']*Ac)

	# Calculate Efficiency and assign column in dataframe
	dataiEFF = datai['Pout']/(datai['Pin'])
	datai = datai.assign(Eff=dataiEFF)

	# Filter data
	dataif = daf.data_filter(datai, BMdatestrs[BMfnum[i]], tistr[i], tfstr[i])
	
	# Collect necessary info
	PoutAve.append(dataif['Pout'].mean())
	PoutStd.append(dataif['Pout'].std())
	PinAve.append(dataif['Pin'].mean())
	PinStd.append(dataif['Pin'].std())
	PyrAve.append(dataif['PyrE'].mean())
	PyrStd.append(dataif['PyrE'].std())
	EffAve.append(dataif['Eff'].mean())
	EffStd.append(dataif['Eff'].std())
	
	# Append data to data variable
	BMdata.append(dataif)

#######################################
# Set up summary dataframe and begin to fill
#######################################
BMsmry =  pd.DataFrame()
BMdtstr = []
BMleg = []

for i in range(0,len(BMlbl)):
	BMdtstr.append(BMdatestrs[BMfnum[i]])
	BMleg.append(BMdatestrs[BMfnum[i]] + ' ' + BMlbl[i])

BMsmry = BMsmry.assign(Date=BMdtstr)
BMsmry = BMsmry.assign(Name=BMlbl)
BMsmry = BMsmry.assign(PoutAve=PoutAve)
BMsmry = BMsmry.assign(PoutStd=PoutStd)
BMsmry = BMsmry.assign(PinAve=PinAve)
BMsmry = BMsmry.assign(PinStd=PinStd)
BMsmry = BMsmry.assign(PyrAve=PyrAve)
BMsmry = BMsmry.assign(PyrStd=PyrStd)
BMsmry = BMsmry.assign(EffAve=EffAve)
BMsmry = BMsmry.assign(EffStd=EffStd)

############################################################################################
# Benchmark Plots
############################################################################################
if BM == 1:
	
	#######################################
	# Power Output over run time
	#######################################
	if TimePout == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1
		
		for i in range(0, BMnumf):
			plt.plot(BMdata[i]['RunTime'], BMdata[i]['Pout'])
		
		plt.xlabel('Run Time [min]')
		plt.ylabel('Power Output [W]')
		
		plt.legend(BMleg, ncol=2, loc='lower right')

		if figtitles == 1:
			plt.title('All Available Power Benchmark Data')

	
	#######################################
	# Power input over run time
	#######################################
	if TimePin == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1
		
		for i in range(0, BMnumf):
			plt.plot(BMdata[i]['RunTime'], BMdata[i]['Pin'])
		plt.xlabel('Run Time [min]')
		plt.ylabel('Power Input [W]')
		plt.legend(BMleg, ncol=2, loc='lower right')

		if figtitles == 1:
			plt.title('Power Input on a Single Collector (A$_{Collector}$= '+ '%0.3f' % Ac + ' m$^2$)')			

	#######################################
	# Power input vs power output
	#######################################
	if PinPout == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1
		
		# Plot all data
		for i in range(0, BMnumf):
			plt.scatter(BMdata[i]['Pin'], BMdata[i]['Pout'])
		plt.xlabel('Power Input [W]')
		plt.ylabel('Power Output[W]')
		plt.legend(BMleg, ncol=2, loc='upper left')
		plt.xlim([0, 300])
		plt.savefig(figrootname + 'BM_AllPinPout.png')

		if figtitles == 1:
			plt.title('Power Input vs. Power Output for all Benchmarks')
		

	#######################################
	# Average Power input vs power output
	#######################################
	if AvePinPout == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1

		for i in range(0, BMnumf):
			plt.errorbar(BMsmry['PinAve'][i], BMsmry['PoutAve'][i], xerr = BMsmry['PinStd'][i], yerr = BMsmry['PoutStd'][i], fmt='o')
		plt.legend(BMleg, ncol=2, loc='upper left')
		daf.linreg(BMsmry['PinAve'], BMsmry['PoutAve'], 0, 0)
		
		plt.xlim([0, 300])
		plt.xlabel('Power Input [W]')
		plt.ylabel('Power Output[W]')
		
		if figtitles == 1:
			plt.title('Averaged Power Input vs. Power Output')
	
	#######################################
	# Power input vs efficiency
	#######################################
	if PinEff == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1
		
		for i in range(0, BMnumf):
			plt.scatter(BMdata[i]['Pin'], BMdata[i]['Eff'])
		plt.xlabel('Power Input [W]')
		plt.ylabel('Efficiency [%]')
		plt.legend(BMleg, ncol=2, loc='upper left')
		plt.xlim([0, 300])

		if figtitles == 1:
			plt.title('Power Input vs. Efficiency')
	
		plt.savefig(figrootname + 'BM_PinEff.png')
	
	#######################################
	# Average Power input vs efficiency
	#######################################
	if AvePinEff == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1

		for i in range(0, BMnumf):
			plt.errorbar(BMsmry['PinAve'][i], BMsmry['EffAve'][i], xerr = BMsmry['PinStd'][i], yerr = BMsmry['EffStd'][i], fmt='o')
		plt.legend(BMleg, ncol=2, loc='upper left')
		
		plt.xlabel('Power Input [W]')
		plt.ylabel('Efficiency [%]')

		if figtitles == 1:
			plt.title('Average Power Input vs. Efficiency for Benchmarks')

		plt.savefig(figrootname + 'BM_AvePinEff.png')

	#######################################
	# Efficiency vs. power
	#######################################
	if EffPout == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1
		
		for i in range(0, BMnumf):
			plt.scatter(BMdata[i]['Eff'], BMdata[i]['Pout'])
		plt.xlabel('Efficiency [%]')
		plt.ylabel('Power Output [W]')
		plt.legend(BMleg, ncol=2, loc='upper left')
		plt.ylim([0,90])
		daf.linreg(BMdata[i]['Eff'], BMdata[i]['Pout'], 0, 0)

		if figtitles == 1:
			plt.title('Efficiency vs. Power Output for Benchmarks')

	#######################################
	# Average Efficiency vs. power
	#######################################
	if AveEffPout == 1:
		# Plot average data
		plt.figure(figi)
		figi += 1

		for i in range(0, BMnumf):
			plt.errorbar(BMsmry['EffAve'][i], BMsmry['PoutAve'][i], xerr = BMsmry['EffStd'][i], yerr = BMsmry['PoutStd'][i], fmt='o')
		plt.legend(BMleg, ncol=2, loc='upper left')
		
		# Optional trendline
		if False:
			daf.linreg(smry['EffAve'], smry['PoutAve'], 0, 0)
		
		plt.xlabel('Efficiency [%]')
		plt.ylabel('Power Output[W]')

		if figtitles == 1:
			plt.title('Average Efficiency vs. Power Output for Benchmark Averages')

	
##############################################################################
##############################################################################
##############################################################################
# Subset: plot a subset of all data
##############################################################################
##############################################################################
##############################################################################

# In this case, we're plotting the collector/fiber pairs we use in experimentation as well as high irradiance data

if SubSet == 1:

	# Necessary variables
	SSn = ['C1 FC', 'C2 FA', 'C3 FF', 'C4 FD'] # Subset labels
	SSmkrs = ['o', '^', 's', 'X'] # subset markers

	##############################################################################
	# Filter data for subsets of interest
	##############################################################################
	
	#######################################
	# Declare variables for CF pairs of interest
	#######################################
	SSdata = [] # Subset data
	SSdatestrs = [] # Subset dates
	SSleg = [] # Initiate legend vector

	SSPoutAve = [] # Average Power Output
	SSPoutStd = [] # Power output standard deviation
	SSPinAve = [] # Average power input
	SSPinStd = [] # Power input standard deviaiton 
	SSPyrAve = [] # Average irradiance
	SSPyrStd = [] # Irradiance Standard deviation
	SSEffAve = [] # Average effciciency
	SSEffStd = [] # Efficiency standard deviation
	
	#######################################
	# Declare variables for data filtered above an irradiance threshold
	#######################################
	PyHiThreshold = 800 # Filter Threshold
	SSdata_PyHi = [] # Subset data filtered for high pyrheliometer readings
	SSPoutAve_PyHi = [] # Average Power Output
	SSPoutStd_PyHi = [] # Power output standard deviation
	SSPinAve_PyHi = [] # Average power input
	SSPinStd_PyHi = [] # Power input standard deviaiton
	SSPyrAve_PyHi = [] # Average irradiance reading
	SSPyrStd_PyHi = [] # Irradiance standard deviation
	SSEffAve_PyHi = [] # Average effciciency
	SSEffStd_PyHi = [] # Efficiency standard deviation
	
	#######################################
	# Create summary variables for select datasets 
	#######################################
	for i in range(0, len(SSn)):
		SSdata.append(pd.DataFrame()) # Create a dataframe for each collector/fiber pair within SSdata
		SSdatestrs.append([])
		SSleg.append([])
		
		# Create power, pyr and efficiency indices for each collector/fiber pair
		SSPoutAve.append([])
		SSPoutStd.append([])
		SSPinAve.append([])
		SSPinStd.append([])
		SSPyrAve.append([])
		SSPyrStd.append([])
		SSEffAve.append([])
		SSEffStd.append([])

		SSdata_PyHi.append(pd.DataFrame()) # Create a dataframe for each collector/fiber pair for data filtered for high pyrheliometer readings

		# Create indices for high irradiance data
		SSPoutAve_PyHi.append([])
		SSPoutStd_PyHi.append([])
		SSPinAve_PyHi.append([])
		SSPinStd_PyHi.append([])
		SSPyrAve_PyHi.append([])
		SSPyrStd_PyHi.append([])
		SSEffAve_PyHi.append([])
		SSEffStd_PyHi.append([])

	#######################################
	# Select and filter data and calculate summary information
	#######################################
	for i in range(0, len(SSn)):
		for j in range(0, BMnumf):
			
			# Choose data of interest to select from benchmark data
			if SSn[i] in BMlbl[j]:
				
				#######################################
				# Create dataset for each collector/fiber pair
				#######################################
				SSdata[i] = SSdata[i].append(BMdata[j], ignore_index=True) # Combine data from multiple benchmarks into a single dataset for each collector/fiber pair
				SSleg[i].append(BMleg[j]) # Create legend list for each collector/fiber pair
				SSdatestrs[i].append(BMdatestrs[BMfnum[j]]) # Create list of dates for each collector/fiber pair 

				# Average power for each benchmark in one of the selections
				SSPoutAve[i].append(BMdata[j]['Pout'].mean())
				SSPoutStd[i].append(BMdata[j]['Pout'].std())
				SSPinAve[i].append(BMdata[j]['Pin'].mean())
				SSPinStd[i].append(BMdata[j]['Pin'].std())
				SSPyrAve[i].append(BMdata[j]['PyrE'].mean())
				SSPyrStd[i].append(BMdata[j]['PyrE'].std())
				SSEffAve[i].append(BMdata[j]['Eff'].mean())
				SSEffStd[i].append(BMdata[j]['Eff'].std())

				#######################################
				# Filter data above an irradiance threshold set in PyHiThreshold, compile and summarize
				#######################################
				
				# Filter data
				fPyHi = BMdata[j]['PyrE'] > PyHiThreshold # Create filter for pyrheliometer values greater than PyHiThreshold in W/m2
				SSdf_PyHi = BMdata[j].loc[fPyHi] # Pull filtered data
				SSdata_PyHi[i] = SSdata_PyHi[i].append(SSdf_PyHi) # Combine filtered data with other data for that Collector/fiber pair

				# Averages for selctions filered for pyrheliometer data above threshold
				SSPoutAve_PyHi[i].append(SSdf_PyHi['Pout'].mean())
				SSPoutStd_PyHi[i].append(SSdf_PyHi['Pout'].std())
				SSPinAve_PyHi[i].append(SSdf_PyHi['Pin'].mean())
				SSPinStd_PyHi[i].append(SSdf_PyHi['Pin'].std())
				SSPyrAve_PyHi[i].append(SSdf_PyHi['PyrE'].mean())
				SSPyrStd_PyHi[i].append(SSdf_PyHi['PyrE'].std())
				SSEffAve_PyHi[i].append(SSdf_PyHi['Eff'].mean())
				SSEffStd_PyHi[i].append(SSdf_PyHi['Eff'].std())

	########################################
	# Calculate flat average efficiencies of all select data
	########################################
	# Benchmark data
	CFPoutAve = [] # Average Power Output
	CFPoutStd = [] # Power output standard deviation
	CFPinAve = [] # Average Power input
	CFPinStd = [] # Power input standard deviation
	CFPyrAve = [] # Average pyrheliometer reading
	CFPyrStd = [] # pyrheliometer standard deviaiton 
	CFEffAve = [] # Average effciciency
	CFEffStd = [] # Efficiency standard deviation

	# Benchmark data filtered for irradiance values above a  threshold set with PyHiThreshold
	CFPyHiPoutAve = [] # Average Power Output
	CFPyHiPoutStd = [] # Power output standard deviation
	CFPyHiPinAve = [] # Average Power Input
	CFPyHiPinStd = [] # Power input standard deviation
	CFPyHiPyrAve = [] # Average pyrheliometer reading
	CFPyHiPyrStd = [] # pyrheliometer standard deviaiton 
	CFPyHiEffAve = [] # Average effciciency
	CFPyHiEffStd = [] # Efficiency standard deviation
	
	# Create flat averages for each collector/fiber pair
	for i in range(0, len(SSn)):
		CFPoutAve.append(np.mean(SSPoutAve[i])) 
		CFPoutStd.append(np.std(SSPoutStd[i]))
		CFPinAve.append(np.mean(SSPinAve[i])) 
		CFPinStd.append(np.std(SSPinStd[i]))
		CFPyrAve.append(np.mean(SSPyrAve[i]))
		CFPyrStd.append(np.std(SSPyrStd[i]))
		CFEffAve.append(np.mean(SSEffAve[i]))
		CFEffStd.append(np.std(SSEffAve[i]))

		# Filtered data above a given threshold
		CFPyHiPoutAve.append(np.mean(SSPoutAve_PyHi[i])) 
		CFPyHiPoutStd.append(np.std(SSPoutStd_PyHi[i]))
		CFPyHiPinAve.append(np.mean(SSPinAve_PyHi[i]))
		CFPyHiPinStd.append(np.std(SSPinStd_PyHi[i]))
		CFPyHiPyrAve.append(np.mean(SSPyrAve_PyHi[i]))
		CFPyHiPyrStd.append(np.std(SSPyrStd_PyHi[i]))
		CFPyHiEffAve.append(np.mean(SSEffAve_PyHi[i]))
		CFPyHiEffStd.append(np.std(SSEffAve_PyHi[i]))

	########################################
	# Output collector/fiber summaries to dataframe
	########################################
	CFsmry = pd.DataFrame() # Declare a dataframe
	CFsmry = CFsmry.assign(CollectorFibers=SSn) # Dataset name

	# Average Power inputs, outputs, irradiances and efficiencies
	CFsmry = CFsmry.assign(PoutAve=CFPoutAve)
	CFsmry = CFsmry.assign(PoutStd=CFPoutStd)
	CFsmry = CFsmry.assign(PyrAve=CFPyrAve)
	CFsmry = CFsmry.assign(PyrStd=CFPyrStd)
	CFsmry = CFsmry.assign(EffAve=CFEffAve)
	CFsmry = CFsmry.assign(EffStd=CFEffStd)

	# Ave Power inputs, outputs and efficiencies for PyHi
	CFsmry = CFsmry.assign(PyHi_PoutAve=CFPyHiPoutAve)
	CFsmry = CFsmry.assign(PyHi_PoutStd=CFPyHiPoutStd)
	CFsmry = CFsmry.assign(PyHi_PyrAve=CFPyHiPyrAve)
	CFsmry = CFsmry.assign(PyHi_PyrStd=CFPyHiPyrStd)
	CFsmry = CFsmry.assign(PyHi_EffAve=CFPyHiEffAve)
	CFsmry = CFsmry.assign(PyHi_EffStd=CFPyHiEffStd)

	########################################
	# Build trendline coefficients from subset data
	#######################################
	# Declare linear Trendline Coefficient and R-squared variables
	TLC = np.empty((len(SSn), 2))
	TLr2 = np.empty((len(SSn)))

	TLC_PyHi = np.empty((len(SSn), 2))	
	TLr2_PyHi = np.empty((len(SSn)))

	# Declare Quadratic trendline coefficients and r-squared variables
	QLC = np.empty((len(SSn), 3))
	QLr2 = np.empty((len(SSn)))

	QLC_PyHi = np.empty((len(SSn), 3))
	QLr2_PyHi = np.empty((len(SSn)))

	# Calculate trendline coefficients and r-squared values
	for i in range(0, len(SSn)):
		# Linear trendline
		TLC[i:] = daf.linreg(SSdata[i]['Pin'], SSdata[i]['Pout'], 0, 0, p=False)

		TLr2[i] = daf.rsquared(SSdata[i]['Pin'],  SSdata[i]['Pout'], TLC[i,0], TLC[i,1])

		TLC_PyHi[i:] = daf.linreg(SSdata_PyHi[i]['Pin'], SSdata_PyHi[i]['Pout'], 0, 0, p=False)

		TLr2_PyHi[i] = daf.rsquared(SSdata_PyHi[i]['Pin'],  SSdata_PyHi[i]['Pout'], TLC_PyHi[i,0], TLC_PyHi[i,1])
		
		# Quadratic Trendline
		QLC[i:] = daf.quadreg(SSdata[i]['Pin'], SSdata[i]['Pout'], 0, 0, p=False) # Quadratic regression coefficients for a particular collector/fiber pair

		QLC_PyHi[i:] = daf.quadreg(SSdata_PyHi[i]['Pin'], SSdata_PyHi[i]['Pout'], 0, 0, p=False)

	########################################
	# Output trendline coefficients to dataframe
	#######################################

	# Trendline coefficients
	CFsmry = CFsmry.assign(TL_C0=TLC[:,0])
	CFsmry = CFsmry.assign(TL_C1=TLC[:,1])
	CFsmry = CFsmry.assign(QL_C0=QLC[:,0])
	CFsmry = CFsmry.assign(QL_C1=QLC[:,1])
	CFsmry = CFsmry.assign(QL_C2=QLC[:,2])

	# High irradiance TL coefficients
	CFsmry = CFsmry.assign(TL_C0_PyHi=TLC_PyHi[:,0])
	CFsmry = CFsmry.assign(TL_C1_PyHi=TLC_PyHi[:,1])
	CFsmry = CFsmry.assign(QL_C0_PyHi=QLC_PyHi[:,0])
	CFsmry = CFsmry.assign(QL_C1_PyHi=QLC_PyHi[:,1])
	CFsmry = CFsmry.assign(QL_C1_PyHi=QLC_PyHi[:,2])

	##############################################################################
	# Plots
	##############################################################################

	########################################
	# Plot average efficiencies for each CF pair on a Bar chart. Compares unfiltered data with high irradiance data
	#######################################
	if CFEff == 1:
		# Create new figure
		plt.figure()
		figi += 1

		# Create positions for bars
		bar_loc = np.arange(0, len(CFsmry))

		# Plot both types of efficiency
		plt.bar(bar_loc+0.125, CFsmry['EffAve']*100, yerr = CFsmry['EffStd']*100, capsize=4, width=0.25, color=CUclrs[0])
		plt.bar(bar_loc-0.125, CFsmry['PyHi_EffAve']*100, yerr = CFsmry['PyHi_EffStd']*100, capsize=4, width=0.25, color=CUclrs[1])
		
		# Plot parameters
		plt.ylabel('Efficiency [%]')
		plt.xlabel('Collector/Fiber Configuration')
		plt.xticks(bar_loc, SSn)
		plt.legend(['Overall Average', 'Filtered for Irradiances >' + str(PyHiThreshold)], loc='upper right')
		plt.ylim([0,31])

		if figtitles == 1:
			plt.title('Average Efficiencies for Select Collector/Fiber Pairs')

		
		# Build Labels for the top of each bar
		for i in range(0, len(bar_loc)):
			FAtloc = CFsmry['EffAve'][i]*100 + CFsmry['EffStd'][i]*100 + 0.25
			FAvalstr = f"{CFsmry['EffAve'][i]*100:.1f}" +'%'
			plt.text(bar_loc[i]+0.125, FAtloc, FAvalstr, horizontalalignment='center')

			PHtloc = CFsmry['PyHi_EffAve'][i]*100 + CFsmry['PyHi_EffStd'][i]*100 + 0.25
			PHvalstr = f"{CFsmry['PyHi_EffAve'][i]*100:.1f}" +'%'
			plt.text(bar_loc[i] - 0.125, PHtloc, PHvalstr, horizontalalignment='center')

		plt.savefig(figrootname + 'BM_CF_Eff_BarComparison.png')

	#######################################
	# Power in vs. Power out for for all Select Collector/Fiber Pairs
	#######################################
	if SSPinPout == 1:
		# Create figure
		plt.figure(figi)
		figi += 1

		citer = 0 # Color iterator
		# Plot all data of interest 
		for i in range(0, BMnumf):
			for j in range(0, len(SSn)):
				if SSn[j] in BMlbl[i]:
					
					plt.scatter(BMdata[i]['Pin'], BMdata[i]['Pout'], marker=SSmkrs[j], edgecolor = clrs[citer], alpha=0.25)
					citer +=1
		
		# Plot settings
		plt.xlabel('Power Input [W]')
		plt.ylabel('Power Output [W]')
		plt.legend(SSleg[0] + SSleg[1] + SSleg[2] + SSleg[3], loc='upper left')
		plt.xlim([0, 300])

		if figtitles == 1:
			plt.title('Power Input vs. Power Output for Select Collector/Fiber Pairs')

		plt.savefig(figrootname + 'BM_SelectCFs_PinPout.png')
	
	########################################
	# Power In vs Power Out with each CF pair on its own subplot with trendline
	########################################	
	if SSPinPoutSubplot == 1:
		plt.figure(figi)
		figi += 1
		
		# Data sets to plot
		for i in range(0, BMnumf):
			for j in range(0, len(SSn)):
				
				# Data sets to exclude 
				# if (leg[i] == '220324 C1 FC') or (leg[i] == '220313 C1 FC'):
				# 	continue
				
				if SSn[j] in BMlbl[i]:
					plt.subplot(2,2,j+1)
					plt.scatter(BMdata[i]['Pin'], BMdata[i]['Pout'])
			
	
		for i in range(0, len(SSn)):
			plt.subplot(2,2,i+1)
			plt.xlabel('Power Input [W]')
			plt.ylabel('Power Output[W]')
			plt.suptitle('Benchmark Power Data with Trendlines')
			plt.legend(SSleg[i], loc='upper left')
			daf.linreg(SSdata[i]['Pin'], SSdata[i]['Pout'], 200, 10) # plot trentline, output coefficients

			if figtitles == 1:
				plt.title(SSn[i])
		plt.subplots_adjust(hspace=0.3)
		plt.savefig(figrootname + 'BM_SelectCF_Subplots.png')
	
	########################################
	# Power In vs. Efficiency for each CF pair in its own subplot with linear and quadratic trendlines
	#######################################
	if SSPinEff == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1
		
		# Data sets to plot
		for i in range(0, BMnumf):
			for j in range(0, len(SSn)):
				
				# Data sets to exclude 
				# if (leg[i] == '220324 C1 FC') or (leg[i] == '220313 C1 FC'):
				# 	continue
				
				if SSn[j] in BMlbl[i]:
					plt.subplot(2,2,j+1)
					plt.scatter(BMdata[i]['Eff'], BMdata[i]['Pin'])
		
		
		for i in range(0, len(SSn)):
			plt.subplot(2,2,i+1)
			plt.xlabel('Efficiency')
			plt.ylabel('Power Input [W]')
			plt.legend(SSleg[i], loc='upper left')
			daf.linreg(SSdata[i]['Eff'], SSdata[i]['Pin'], 0, 0)
			daf.quadreg(SSdata[i]['Eff'], SSdata[i]['Pin'], 0, 0)

			if figtitles == 1:
				plt.title('Power Input vs. Efficiency for ' + SSn[i])

		plt.subplots_adjust(hspace=0.3)

	########################################
	# Efficiency vs Power out with each CF on its own subplot with linear and quadratic trendlines
	#######################################
	if SSPowOutEff == 1:
		# Create new figure
		plt.figure(figi)
		figi += 1
		
		# Data sets to plot
		for i in range(0, BMnumf):
			for j in range(0, len(SSn)):
				
				# Data sets to eliminate 
				# if (leg[i] == '220324 C1 FC') or (leg[i] == '220313 C1 FC'):
				# 	continue
				
				if SSn[j] in BMlbl[i]:
					plt.subplot(2,2,j+1)
					plt.scatter(BMdata[i]['Eff'], BMdata[i]['Pout'])
		
		for i in range(0, len(SSn)):
			plt.subplot(2,2,i+1)
			plt.xlabel('Efficiency')
			plt.ylabel('Power Output [W]')
			plt.legend(SSleg[i], loc='upper left')
			daf.linreg(SSdata[i]['Eff'], SSdata[i]['Pout'], 0, 0)
			daf.quadreg(SSdata[i]['Eff'], SSdata[i]['Pout'], 0, 0)

			if figtitles == 1:
				plt.title('Efficiency vs. Power Output for ' + SSn[i])

		plt.subplots_adjust(hspace=0.35)
	
	########################################
	# Average Power in vs Power out with each CF on its own subplot with linear trendlines
	#######################################
	if SSAvePowInPowOut == 1:
		# Create new figure 
		plt.figure(figi)
		figi += 1
		
		# Data sets to plot
		for i in range(0, len(SSn)):
			for j in range(0, len(SSPinAve[i])):
				# Data sets to exclude 
				# if (leg[i] == '220324 C1 FC') or (leg[i] == '220313 C1 FC'):
				# 	continue

				plt.subplot(2,2,i+1)
				plt.errorbar(SSPinAve[i][j], SSPoutAve[i][j], xerr = SSPinAve[i][j], yerr = SSPoutStd[i][j], fmt='o')
					
		for i in range(0, len(SSn)):
			plt.subplot(2,2,i+1)
			plt.xlabel('Power Input [W]')
			plt.ylabel('Power Output [W]')
			plt.legend(SSleg[i], loc='lower right')
			daf.linreg(SSPinAve[i], SSPoutAve[i], 0, 0)

			if figtitles == 1:
				plt.title('P$_{in}$ vs P$_{out}$ for ' + SSn[i])
		
		plt.subplots_adjust(hspace=0.275)


##############################################################################
##############################################################################
##############################################################################
# Experimental Data
##############################################################################
##############################################################################
##############################################################################


if ExpData == 1:
	#######################################
	# Create file index for each dataset
	#######################################
	efnum = []
	for i in range(0, len(enames)):
		for j in range(0, len(elblidx[i])):
			efnum.append(i)
	
	#######################################
	# Set up summary data frame and begin to fill
	#######################################
	enumf = len(elbl) # Number of filtered datasets 
	
	edtstr = [] # List of date strings
	eleg = [] # List of legends

	# Create date and legend lists
	for i in range(0, enumf):
		edtstr.append(edatestrs[efnum[i]])
		eleg.append(edatestrs[efnum[i]] + ' ' + elbl[i])

	# Fill dataframe with date, name and collector information
	esmry =  pd.DataFrame()
	esmry = esmry.assign(Date=edtstr)
	esmry = esmry.assign(Name=eleg)
	esmry = esmry.assign(CollectorFibers = cfstr)
	
	#######################################
	# Read and filter data for time while sunlight is being collected
	#######################################
	# Initiate summary variables
	edata = [] # Data variable
	ePinAve = [] # Average power in
	ePinStd = [] # Standard deviaiton of power in
	ePyrAve = [] # Average irradiance
	ePyrStd = [] # Irradiance standard deviation

	for i in range(0, enumf):
		# Read and format data
		edatai = daf.data_read_format(efpath + enames[efnum[i]], edatestrs[efnum[i]])

		#  Calculate Power in and create a column for it in the dataframe
		edatai = edatai.assign(Pin=edatai['PyrE']*Ac)

		# Calculate power output estimations and assign to dataframe
		for j in range(0, len(SSn)):
			# Pout Calculated with trend line
			hnTL = 'PoutEst_TL_' + SSn[j].replace(' ', '') # Header name
			edatai = edatai.assign(**{hnTL: edatai['Pin']*TLC[j,0] + TLC[j,1]})

			# Pout Calculated with Flat Average efficiency 
			hnFA = 'PoutEst_FA_' + SSn[j].replace(' ', '') # Header name
			edatai = edatai.assign(**{hnFA: edatai['Pin']*CFEffAve[j]})

			# Pout Calculated with FA efficiency filtered for high irradiances
			hnPyHi = 'PoutEst_PyHi_' + SSn[j].replace(' ', '') # Header name
			edatai = edatai.assign(**{ hnPyHi: edatai['Pin']*CFPyHiEffAve[j] })

		# Filter data to meet times of interest
		edataif = daf.data_filter(edatai, edatestrs[efnum[i]], etistr[i], etfstr[i])

		# Create summary lists
		ePyrAve.append(edataif['PyrE'].mean())
		ePyrStd.append(edataif['PyrE'].std())
		ePinAve.append(edataif['Pin'].mean())
		ePinStd.append(edataif['Pin'].std())

		# Add data from experiment i to edata variable
		edata.append(edataif)

	# Output Aves and Stds to summary dataframe
	esmry = esmry.assign(PinAve=ePinAve) # Average power in 
	esmry = esmry.assign(PinStd=ePinStd) # Power in standard deviation 
	esmry = esmry.assign(PyrAve=ePyrAve) # Average irradiance data
	esmry = esmry.assign(PyrStd=ePyrStd) # Irradiance standard deviaiton

	#######################################
	# Output summaries of Power output calculated via trendline, flat efficiency and FA filtered for high irradiance
	#######################################
	for i in range(0, len(SSn)):
		TLave = []
		TLstd = []
		FAave = []
		FAstd = []
		PyHiave = []
		PyHistd = []
		hnTL = 'PoutEst_TL_' + SSn[i].replace(' ', '') # Header name
		hnFA = 'PoutEst_FA_' + SSn[i].replace(' ', '') # Header name
		hnPyHi = 'PoutEst_PyHi_' + SSn[i].replace(' ', '') # Header name

		for j in range(0, enumf):
			TLave.append(edata[j][hnTL].mean())
			TLstd.append(edata[j][hnTL].std())
			FAave.append(edata[j][hnFA].mean())
			FAstd.append(edata[j][hnFA].std())
			PyHiave.append(edata[j][hnPyHi].mean())
			PyHistd.append(edata[j][hnPyHi].std())

		esmry = esmry.assign(**{hnTL +'_Ave': TLave})
		esmry = esmry.assign(**{hnTL +'_Std': TLstd})
		esmry = esmry.assign(**{hnFA +'_Ave': FAave})
		esmry = esmry.assign(**{hnFA +'_Std': FAstd})
		esmry = esmry.assign(**{hnPyHi +'_Ave': PyHiave})
		esmry = esmry.assign(**{hnPyHi +'_Std': PyHistd})


	##############################################################################
	# Plots
	##############################################################################


	#######################################
	# Plot irradiances for each experiment in its own window and show time filtered data on top of unfiltered data
	#######################################
	# *** This plot creates a lot of windows!!! ***
	if ExpShowFilters == 1:
		
		# Loop through each experiment
		for i in range(0, enumf):
			# Create new figure  
			plt.figure(figi)
			figi += 1
			
			plt.scatter(datai['Time'], datai['PyrE'])
			plt.scatter(dataif['Time'], dataif['PyrE'])
			plt.xlabel('Time [MDT]')
			plt.ylabel(['Pyrheliometer Reading [W/m$^2$]'])
			plt.legend(['Unfiltered Data', 'Data Filtered for Time Collectors Uncovered'], loc='lower left')

			if figtitles == 1:
				plt.title('Pyrheliometer Reading for Experiment ' + eleg[i])

	#######################################
	# Plot Average power input for each experiment on a bar chart
	#######################################
	if ExpPinBar == 1:
		# Set up figure
		plt.figure()
		figi += 1

		# Create Legend
		plt.barh(0, 0, color=CUclrs[0])
		plt.barh(0, 0, color=CUclrs[1])
		plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$') # Snowflake
		plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$') # Thunderbolt
		plt.legend( ['No Ignition', 'Ignition', 'GAC', 'Petroleum'] , loc='upper left')

		# Locations for bars
		bar_loc = np.arange(0, enumf)

		# Plot parameters
		for i in range(0, enumf):
			if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
				plt.bar(bar_loc[i], esmry['PinAve'][i], yerr=esmry['PinStd'][i], capsize=4, color=CUclrs[1])
			else:
				plt.bar(bar_loc[i], esmry['PinAve'][i], yerr=esmry['PinStd'][i], capsize=4, color=CUclrs[0])
		plt.ylabel('Average Power Input [W]')
		plt.xlabel('Experiment ID')
		plt.xticks(bar_loc, expID)

		if figtitles == 1:
			plt.title('Average Power Input During Each Experiment for a Single Collector (A$_{Collector}$= '+ '%0.3f' % Ac + ' m$^2$)')
		
		# Create labels on top of bars
		tloc = esmry['PinAve'] + esmry['PinStd'] # Text location
		tloc = tloc * 1.01

		for i in range(0, enumf):
			plt.text(bar_loc[i] , tloc[i], '%0.1f' % (esmry['PinAve'][i]), horizontalalignment='center')
		
			tloc[i] = tloc[i] + 10
			# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
			if igstr[i] == 'Ignition':
				plt.text( bar_loc[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size = 16)
			elif igstr[i] == 'No':
				plt.text(bar_loc[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size = 16)
			elif igstr[i] == 'Ignition without Propegation':
				plt.text(bar_loc[i], tloc[i], '\u26A1  ', c='r', horizontalalignment='center', size = 16)
				plt.text(bar_loc[i], tloc[i], '  \u2744', c='c', horizontalalignment='center', size = 16)
			else:
				plt.text(bar_loc[i], tloc[i], '????', c='r', horizontalalignment='center', size = 16)

		plt.ylim(0,350)
		plt.savefig(figrootname + 'Exp_AvePowIn_Bar.png')
	
	#######################################
	# Plots Power in vs. Power out for each CF pair in its own window with trendlines with separate windows for each CF
	#######################################
	if PinPoutTLs == 1:
		
		# Trendline text locations
		TLtx = [205, 205, 205, 205]
		TLty = [68, 60, 65, 62]
		FAtx = [150, 150, 150, 150]
		FAty = [54, 46, 55, 49]
		PyHitx = [75, 75, 75, 75]
		PyHity = [41, 33, 42, 37]
		
		# Loop through each CF pair
		for i in range(0, len(SSn)):
			# Create new figure 
			plt.figure(figi)
			figi+= 1
						
			# Plot benchmark data
			plt.scatter(SSdata[i]['Pin'], SSdata[i]['Pout'], c=CUclrs[0])

			# Calculate R-squared values for Flat Average efficiencies
			FA_r2 = daf.rsquared(SSdata[i]['Pin'], SSdata[i]['Pout'], CFsmry['EffAve'][i], 0)
			PyHi_r2 = daf.rsquared(SSdata[i]['Pin'], SSdata[i]['Pout'], CFsmry['PyHi_EffAve'][i], 0)			

			# Plot Trendlines with labels
			daf.linreg(SSdata[i]['Pin'], SSdata[i]['Pout'], TLtx[i], TLty[i])

			TLx = np.arange(SSdata[i]['Pin'].min(), SSdata[i]['Pin'].max())
			plt.plot(TLx, CFsmry['EffAve'][i]*TLx, 'b:')
			plt.text(FAtx[i], FAty[i], 'y = ' + '%0.3F' % CFsmry['EffAve'][i] + 'x\nR$^2$ = '+ '%0.2F' % FA_r2  + '\nOverall Average Efficiency', c='b') 
			plt.plot(TLx, CFsmry['PyHi_EffAve'][i]*TLx, 'g-.')
			plt.text(PyHitx[i], PyHity[i], 'y = ' + '%0.3F' % CFsmry['PyHi_EffAve'][i] + 'x\nR$^2$ = '+ '%0.2F' % PyHi_r2  + '\nEfficiency filtered for high irradiances', c='g')

			# Plot parameters
			plt.xlabel('Power Input [W]')
			plt.ylabel('Power Output [W]')

			if figtitles == 1:
				plt.title('Benchmark Power In vs. Power Out for ' + SSn[i])

			plt.savefig(figrootname + 'BM_PinPoutTLs_Unfiltered' + SSn[i] + '.png')

	#######################################
	# XXXXX Create Ploot power in vs. power out for benchmarks with unfiltered data and data filtered for high irradiances with separate windows for each CF
	#######################################
	if PinPoutTLs_WithPyHi == 1:
		
		# Loop through each CF pair
		for i in range(0, len(SSn)):
			# Create new figure 
			plt.figure(figi)
			figi+= 1
						
			# Plot benchmark data
			plt.scatter(SSdata[i]['Pin'], SSdata[i]['Pout'], c=CUclrs[0])
			
			# Plot high irradiance data
			plt.scatter(SSdata_PyHi[i]['Pin'], SSdata_PyHi[i]['Pout'], c=CUclrs[1])

			# Calculate R-squared values for Flat Average efficiencies
			FA_r2 = daf.rsquared(SSdata[i]['Pin'], SSdata[i]['Pout'], CFsmry['EffAve'][i], 0)
			PyHi_r2 = daf.rsquared(SSdata[i]['Pin'], SSdata[i]['Pout'], CFsmry['PyHi_EffAve'][i], 0)			

			# Plot Trendlines with labels
			daf.linreg(SSdata[i]['Pin'], SSdata[i]['Pout'], TLtx[i], TLty[i])

			TLx = np.arange(SSdata[i]['Pin'].min(), SSdata[i]['Pin'].max())
			plt.plot(TLx, CFsmry['EffAve'][i]*TLx, 'b:')
			plt.text(FAtx[i], FAty[i], 'y = ' + '%.1F' % (CFsmry['EffAve'][i]*100) + 'x\nR$^2$ = '+ '%0.2F' % FA_r2  + '\nOverall Average Efficiency', c='b') 
			plt.plot(TLx, CFsmry['PyHi_EffAve'][i]*TLx, 'g-.')
			plt.text(PyHitx[i], PyHity[i], 'y = ' + '%.1F' % (CFsmry['PyHi_EffAve'][i]*100) + 'x\nR$^2$ = '+ '%0.2F' % PyHi_r2  + '\nEfficiency filtered for high irradiances', c='g')

			# Plot parameters
			plt.xlabel('Power Input [W]')
			plt.ylabel('Power Output [W]')
			plt.legend(['Unfiltered', 'Irradiances Above ' + str(PyHiThreshold)])

			if figtitles == 1:
				plt.title('Benchmark Power In vs. Power Out for ' + SSn[i] + 'with High Irradiance Data')

			plt.savefig(figrootname + 'BM_PinPoutTLs_UnfilteredWithPyHi' + SSn[i] + '.png')


	#######################################
	# Plot power in vs. power out for benchmarks filtered for high irradiances with separate windows for each CF
	#######################################
	if PyHiPinPoutTLs == 1:
		
		# Trendline label locations
		TLtx = [260, 260, 260, 260]
		TLty = [55, 49, 62, 55]
		FAtx = [260, 260, 260, 260]
		FAty = [50, 44.5, 58.5, 52.5]
		PyHitx = [260, 260, 260, 260]
		PyHity = [45, 40, 55, 50]

		# Cycle through CF pairs
		for i in range(0, len(SSn)):
			# Create new figure
			plt.figure(figi)
			figi += 1

			# Plot data
			plt.scatter(SSdata_PyHi[i]['Pin'], SSdata_PyHi[i]['Pout'], c=CUclrs[1])

			# Plot Trendlines
			daf.linreg(SSdata_PyHi[i]['Pin'], SSdata_PyHi[i]['Pout'], TLtx[i], TLty[i])

			TLx = np.arange(SSdata_PyHi[i]['Pin'].min(),SSdata_PyHi[i]['Pin'].max()) # Trendline x-values
			plt.plot(TLx, CFsmry['EffAve'][i]*TLx, 'b:')
			plt.text(FAtx[i], FAty[i], 'y = ' + '%.1F' % (CFsmry['EffAve'][i]*100) + 'x\nR$^2$ = '+ '%0.2F' % FA_r2  + '\nOverall Average Efficiency', c='b') 
			
			plt.plot(TLx, CFsmry['PyHi_EffAve'][i]*TLx, 'g-.')
			plt.text(PyHitx[i], PyHity[i], 'y = ' + '%.1F' % (CFsmry['PyHi_EffAve'][i]*100) + 'x\nR$^2$ = '+ '%0.2F' % PyHi_r2  + '\nEfficiency filtered for high irradiances', c='g')
			
			# Plot parameters
			plt.xlabel('Power Input [W]')
			plt.ylabel('Power Output [W]')

			if figtitles == 1:
				plt.title('Benchmark Data Filtered for High Irradiance with Trendlines for ' + SSn[i])

			plt.savefig(figrootname + 'BM_PinPoutTLs_PyHi_' + SSn[i] + '.png')

	##########################################
	# Calculate total power for each experiment and plot on a histogram
	##########################################
	if PoutHist == 1:
		# Set up figure
		plt.figure(figi)
		figi += 1

		# Type of power estimation
		PEstType = 'TL' # Trendline
		Pout_Total = [] # Total power output
		# PEstType = 'FA' # Flat Average Efficiency
		# PEstType = 'PyHi' # High irradiance efficiency 

		# Create Legend
		plt.barh(0, 0, color=clrs[3])
		plt.barh(0, 0, color=clrs[4])
		plt.barh(0, 0, color=clrs[5])
		plt.barh(0, 0, color=clrs[6])
		plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$') # Snowflake
		plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$') # Thunderbolt
		plt.legend( ['No Ignition', 'Ignition'] + SSn, loc='upper left')

		# x-axis values for histogram plot
		bar_loc = np.arange(0,enumf) 

		# Find total power output for a given experiment
		for i in range(0, enumf):
			
			# Initialize varialbes
			PTot = 0 # Total power
			tloc = 0 # Find the y-location to put text labels

			for j in range(0, len(SSn)):
				cfn = SSn[j].replace(' ', '')

				# Colors for overlapping errorbars
				if j%2 == 0:
					ec = '#bcbcbc' # Grey
				else:
					ec = 'k'

				# Plot bars 
				if (cfn in cfstr[i]) or (cfstr[i] == 'All Four'):
					CFpowtag = 'PoutEst_' + PEstType + '_' + cfn + '_Ave'
					CFPoutStdtag = 'PoutEst_' + PEstType + '_' + cfn + '_Std'
					plt.bar(bar_loc[i], esmry[CFpowtag][i], yerr=esmry[CFPoutStdtag][i], bottom = PTot, capsize=4, color = clrs[j+3], ecolor=ec)
					PTot += esmry[CFpowtag][i]
					tloc = esmry[CFPoutStdtag][i]
			
			# Text location for labels above bars
			tloc += PTot
			tloc = tloc*1.01

			# Add labels to each bar with value
			plt.text(bar_loc[i], tloc, "%.0f" % PTot, horizontalalignment='center')
			tloc = tloc + 10 # Change tloc for snowflakes and thunderolts
			
			# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
			if igstr[i] == 'Ignition':
				plt.text( bar_loc[i], tloc, '\u26A1', c='r', horizontalalignment='center', size = 16)
			elif igstr[i] == 'No':
				plt.text(bar_loc[i], tloc, '\u2744', c='c', horizontalalignment='center', size = 16)
			elif igstr[i] == 'Ignition without Propegation':
				plt.text(bar_loc[i], tloc, '\u26A1  ', c='r', horizontalalignment='center', size = 16)
				plt.text(bar_loc[i], tloc, '  \u2744', c='c', horizontalalignment='center', size = 16)
			else:
				plt.text(bar_loc[i], tloc, '????', c='r', horizontalalignment='center', size = 16)
			
			# Total power 
			Pout_Total.append(PTot)

		esmry = esmry.assign(**{'PoutTotalEst_' + PEstType:  Pout_Total})

		# Plot parameters
		plt.xticks(bar_loc, expID)
		# plt.yticks(fontsize=14)
		# plt.ylabel('Estimated Power Output [W]', fontweight='bold', fontsize=15)
		plt.ylabel('Estimated Power Output [W]')
		plt.xlabel('Experiment ID')
		plt.ylim(0, max(Pout_Total) + 25)

		if figtitles == 1:
			plt.title('Power Estimations For Each Experiment', fontsize=20)
	
		plt.savefig(figrootname + 'ExpTotalPout_Bar.png')

		if PoutHistCombined == 1:
			# Set up figure
			plt.figure(figi)
			figi += 1

			# Create Legend
			plt.barh(0, 0, color=CUclrs[0])
			plt.barh(0, 0, color=CUclrs[1])
			plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$') # Snowflake
			plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$') # Thunderbolt
			plt.legend( ['No Ignition', 'Ignition', 'GAC', 'Petroleum'], loc='upper left')

			# x-axis values for histogram plot
			bar_loc = np.arange(0,enumf) 

			for i in range(0, enumf):
				if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
					plt.bar(bar_loc[i], esmry['PoutTotalEst_TL'][i], color=CUclrs[1]) # [i], yerr=esmry['PinStd'][i], capsize=4
				else:
					plt.bar(bar_loc[i], esmry['PoutTotalEst_TL'][i], color=CUclrs[0]) # , yerr=esmry['PinStd'][i], capsize=4, 
			
			tloc = esmry['PoutTotalEst_TL'] + 2

			for i in range(0, enumf):
				plt.text(bar_loc[i], tloc[i], "%.0f" % esmry['PoutTotalEst_TL'][i], horizontalalignment='center')

			tloc = esmry['PoutTotalEst_TL'] + 9

			for i in range(0, enumf):
				if igstr[i] == 'Ignition':
					plt.text( bar_loc[i], tloc[i], '\u26A1', c='r', horizontalalignment='center', size = 16)
				elif igstr[i] == 'No':
					plt.text(bar_loc[i], tloc[i], '\u2744', c='c', horizontalalignment='center', size = 16)
				elif igstr[i] == 'Ignition without Propegation':
					plt.text(bar_loc[i], tloc[i], '\u26A1  ', c='r', horizontalalignment='center', size = 16)
					plt.text(bar_loc[i], tloc[i], '  \u2744', c='c', horizontalalignment='center', size = 16)
				else:
					plt.text(bar_loc[i], tloc[i], '????', c='r', horizontalalignment='center', size = 16)
			
			plt.xticks(bar_loc, expID)
			plt.ylabel('Estimated Power Output [W]')
			plt.xlabel('Experiment ID')
			plt.ylim(0, 275)

			if figtitles == 1:
				plt.title('Combined Power Estimations For Each Experiment', fontsize=20)
			
			plt.savefig(figrootname + 'ExpTotalPout_Bar_Combined.png')

			



##############################################################################
##############################################################################
# Output Data to csv files
##############################################################################
##############################################################################

#######################################
# Output summary dataframe
#######################################
print('\n\n***************************************')
print('SUMMARY OF BENCHMARK DATA')
print('***************************************\n')
print(BMsmry)
outfname = __file__ 
outfname = outfname[:-3]
outfname = outfname + '_Benchmark.csv'
BMsmry.to_csv(outfname)

#######################################
# Output subset summary dataframe
#######################################
print('\n\n***************************************')
print('SUMMARY OF COLLECTOR/FIBER DATA')
print('***************************************\n')
print(CFsmry)
CFoutname = __file__
CFoutname = CFoutname[:-3]
CFoutname = CFoutname + '_CollectorFiber.csv'
CFsmry.to_csv(CFoutname)

#######################################
# Output experimental summary dataframe
#######################################
print('\n\n***************************************')
print('SUMMARY OF EXPERIMENT DATA')
print('***************************************\n')
print(esmry)
eofname = __file__
eofname = eofname[:-3]
eofname = eofname + '_Experiment.csv'
esmry.to_csv(eofname)

##############################################################################
# Show plots!
##############################################################################
plt.show()

exit()