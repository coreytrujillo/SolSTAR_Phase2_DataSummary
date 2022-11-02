# Import Libraries
import DAF2 as daf
import pandas as pd
import pysine
import time
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import cv2
import datetime

#######################################
# Import Benchmark and Experimental Data File information
#######################################
from HeaderExperimentData import *


#######################################
# Figure Setup
#######################################
plt.style.use('./FigStyle.mplstyle') # Load figure settings from style file

figi = 1 
enumf = len(elbl)

#######################################
# Create index for each file
#######################################
efnum = []
for i in range(0, len(enames)):
	for j in range(0, len(elblidx[i])):
		efnum.append(i)

#######################################
# Read and filter data 
#######################################
HR_i = [] # High Resolution indices

for i in range(0, enumf):
	if 'High Re' in elbl[i]:
		HR_i.append(i)

Tagstr = []
data = []
for i in range(0, len(HR_i)):
	# Read and format data
	datai = daf.data_read_format(efpath + enames[efnum[HR_i[i]]], edatestrs[efnum[HR_i[i]]])
	
	# Filter out disconnections
	datai = datai.replace(-9999, None) 

	#  Create temperature tag strings
	Tagstr.append([])
	dc = datai.columns
	for j in range(0, len(dc)):
		if 'Temp' in dc[j]:
			Tagstr[i].append(dc[j]) 

	# Filter data
	if Tempi[HR_i[i]] == 0:
		ti = etistr[HR_i[i]]
	else: 
		ti = Tempi[HR_i[i]]

	if Tempf[HR_i[i]] == 0:
		tf = datai['Time'][datai.index.max()].strftime('%H:%M:%S')
	else:
		tf = Tempf[HR_i[i]]

	dataif = daf.data_filter(datai, edatestrs[efnum[HR_i[i]]], ti, tf)
	dataif = dataif.reset_index()
	data.append(dataif)

########################################
# Create animation
########################################
# Figure Settings
anifig = plt.figure(figi, figsize= [12, 6.75]) # Create new figure
figi += 1 # Iterate figure number
plt.subplots_adjust(left= 0.075, right=0.95, wspace=0.275)

# Figure universal variables
framesdir = 'AniFigs/' # Directory for frames
k = 1 # Data index
FPS = 20 # Frames per second
lengif = 20 # Length of video in seconds
framestot = int(FPS*lengif) # Numer of total frames
lendata = len(data[k]) # Length of the data frame
dint = lendata//framestot # Data Interval for frames
imnum = 0 # Number of images 
datestr = data[k]['Time'][0].strftime('%y%m%d') # date string for this data 

# Calculate aeration time
Atime = datetime.datetime.strptime(datestr + ' ' + AirT[HR_i[k]], '%y%m%d %H:%M:%S')
Adt = (Atime - data[k]['Time'][0]).total_seconds()/60 


# Vertical locations of Thermocouples
ZL = [0, 1, 2.5, 5, 7.5, 10, 12.5, 15]
ZC = [0, 1, 2.5, 5, 7.5, 10, 12.5, 15, 17.5]
ZR = ZL

print('here')
# Create each frame
for i in range (0, framestot):
	print('Creating Image ', str(i), 'of', str(framestot))
	plt.clf()
	TL = [] # Left thermocouple column
	TC = [] # Center thermocouple column
	TR = [] # Right thermocouple column
	
	# First seven TCs in each column
	for j in range(0,7):
		TC.append(data[k][Tagstr[k][j]][i*dint]) # Center column
		TL.append(data[k][Tagstr[k][j+7]][i*dint]) # Left column
		TR.append(data[k][Tagstr[k][j+14]][i*dint]) # Right column
	
	# Add upper thermocouples
	TC.append(data[k][Tagstr[k][21]][i*dint])
	TC.append(data[k][Tagstr[k][24]][i*dint])
	TL.append(data[k][Tagstr[k][22]][i*dint])
	TR.append(data[k][Tagstr[k][23]][i*dint])
	
	# Create plot
	plt.suptitle('Experiment ' + expID[HR_i[k]] +  '\nRun Time: ' + '%0.0f' % data[k]['RunTime'][i*dint] + ' mins' )
	plt.subplots_adjust(top=0.83, wspace=0.37)

	##############################
	# Temperature profiles

	# Left half, left panel
	plt.subplot(1,6,1)
	plt.plot(TL, ZL, 'o-', color='#565A5C')
	plt.xlim(0, 750)
	plt.ylim(-0.5, 18)
	plt.title('Left')

	plt.ylabel('Distance above TR [cm]')
	
	# Left half, center panel
	plt.subplot(1,6,2)
	plt.plot(TC, ZC, 'o-', zorder=0, color='#565A5C')
	plt.xlim(0, 750)
	plt.ylim(-0.5, 18)
	plt.title('Center')

	plt.xlabel('Temperature [$^\circ$C]')
	
	plt.scatter(TC[0], ZC[0], c='r') # Plot TC2 on top of profile
	plt.scatter(TC[3], ZC[3], c='c') # Plot TC4 on top of profile
	plt.scatter(TC[6], ZC[6], c='m') # Plot TC6 on top of profile
	
	# Right half, center panel
	plt.subplot(1,6,3)
	plt.plot(TR, ZR, 'o-', color = '#565A5C')
	plt.ylim(-0.5, 18)
	plt.xlim(0, 750)
	plt.title('Right')

	##############################
	# Individual TCs

	# Right half, top panel
	plt.subplot(3,2,2)
	plt.plot(data[k]['RunTime'][1:i*dint], data[k]['Temp7'][1:i*dint], 'm')
	plt.xlim(data[k]['RunTime'][0], data[k]['RunTime'][lendata-1])
	plt.ylim([0, 750])	

	plt.plot([Adt, Adt], [0, 750], 'k:') # Aeration Line


	# Right half, center panel
	plt.subplot(3,2,4)
	plt.plot(data[k]['RunTime'][1:i*dint], data[k]['Temp4'][1:i*dint], 'c')
	plt.xlim(data[k]['RunTime'][0], data[k]['RunTime'][lendata-1])
	plt.ylim([0, 750])
	plt.ylabel('Temperature [$^\circ$C]')
	plt.plot([Adt, Adt], [0, 750], 'k:') # Aeration Line

	# Right half, bottom panel
	plt.subplot(3,2,6)
	plt.plot(data[k]['RunTime'][1:i*dint], data[k]['Temp1'][1:i*dint], 'r')
	plt.ylim([0, 750])
	plt.xlim(data[k]['RunTime'][0], data[k]['RunTime'][lendata-1])
	plt.xlabel('Run Time [mins]')
	plt.plot([Adt, Adt], [0, 750], 'k:') # Aeration Line

	# Save figure
	plt.savefig(framesdir +'fig' + str(i) + '.png')

	# Iterate image number
	imnum += 1

# Check size of images
fname1 = framesdir + 'fig0.png'
img1 = cv2.imread(fname1)
framesize = img1.shape
print('framesize', framesize)

# Create video from frames
out = cv2.VideoWriter(datestr + '_TempDisplay.mp4', cv2.VideoWriter_fourcc('m', 'p', '4', 'v'), FPS, (framesize[1], framesize[0]))

print('out is opened?', out.isOpened())

for i in range (0, imnum):
	img = cv2.imread( framesdir + 'fig' + str(i) + '.png')
	out.write(img)
	print('Figure ' + str(i) + 'of' + str(framestot) + ' written to video?: ' + str(out.isOpened()))

out.release()

#######################################
# Play tone to signify end of script
#######################################
daf.celebrate()
