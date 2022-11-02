#!/usr/bin/env python

# Import Libraries
import DAF2 as daf
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

#######################################
# Import Benchmark and Experimental Data File information
#######################################
from HeaderExperimentData import *

enumf = len(elbl)

#######################################
# Set up plotting parameters
#######################################
# Get color options
[clrs, CUclrs] = daf.defcolors(enumf)

# Color and font settings for plots
mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color = clrs)
plt.style.use('./FigStyle.mplstyle') # Load figure settings from style file
figrootname = './Figures/' # Figure Output name root
figi = 1 # Initiate igure iterator
figtitles = 1 # Include titles on figures


#######################################
# Plot concentration bar chart
#######################################
#  Create figure with two axes
fig, ax = plt.subplots()
ax2 = ax.twinx() # create seocnd y axis
figi += 1

# Create Legend
plt.bar(0, 0, color=CUclrs[0])
plt.bar(0, 0, color=CUclrs[1])
plt.bar(0, 0, color=CUclrs[2])
plt.bar(0, 0, color='w', edgecolor='k')
plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$') # Snowflake
plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$') # Thunderbolt
plt.legend( ['No Ignition', 'Ignition', 'Concentration GAC', 'Concentration Petroleum', 'GAC Bed Depth', 'Clean Cap Depth'])

# x-axis values for histogram plot
bar_loc = np.arange(0, enumf) 
b_width = 0.25

# Plot contaminant concentration with crude oil in separate color than GAC
for i in range(0, enumf):
	if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
		ax.bar(bar_loc[i], conc[i], color=CUclrs[1], width=b_width,)
	else:
		ax.bar(bar_loc[i], conc[i], color=CUclrs[0], width=b_width,)

# Plot parameters  
ax.set_xticks(bar_loc, expID)
ax.set_xlabel('Experiment ID')
ax.set_ylabel('Concentration [g/kg]')
ConcMax = max(conc)+ 25 # Concentration max y value
ax.set_ylim(0, ConcMax)
ax2.spines['left'].set_color(CUclrs[0])
ax.yaxis.label.set_color(CUclrs[0])
ax.tick_params(axis='y', colors=CUclrs[0])

# Plot GAC depth and Clean Cap Depth
Achannel = 329 # Cross sectional area of a single channnel (cm2)
GACdepth = np.array(GACbed)/Achannel
CapDepth = np.array(CleanCap)/Achannel
DepthMax = 3 # Max value for y axis for depths
ax2.bar(bar_loc - b_width, GACdepth, color=CUclrs[2], width=b_width)
ax2.bar(bar_loc + b_width, CapDepth, color='w', edgecolor = 'k', width=b_width)

# Right vertical axis parameters
ax2.set_ylabel('GAC Bed Depth [cm]')
ax2.set_ylim(0, DepthMax)
ax2.spines['right'].set_color(CUclrs[2])
ax2.yaxis.label.set_color(CUclrs[2])
ax2.tick_params(axis='y', colors=CUclrs[2])

# Plot text
tloc_conc = np.array(conc) + 2 # Top of concentration bar
tloc_bed = GACdepth* 1.01 # Top of GAC depth bar
tloc_cap = CapDepth*1.01 # Top of Cap depth bar

# Plot labels on top of each bar
for i in range(0, enumf):
	# Concentration Bar
	ax2.text(bar_loc[i], tloc_conc[i]*DepthMax/ConcMax, conc[i], horizontalalignment='center')
	
	# GAC depth bar
	if GACdepth[i] == 0:
		GACstr = ''
	else:
		GACstr = ' %0.1f' % GACdepth[i]
	ax2.text(bar_loc[i] - b_width, tloc_bed[i], GACstr, horizontalalignment='center')

	# Clean Cap bar label
	if CapDepth[i] == 0:
		Capstr = ''
	else:
		Capstr = ' %0.1f' % CapDepth[i]
	ax2.text(bar_loc[i] + b_width, tloc_cap[i], Capstr, horizontalalignment='center')

	# Determine vertical location for snowflakes
	if tloc_cap[i]*ConcMax/DepthMax >  tloc_conc[i]:
		tloc = tloc_cap[i]*ConcMax/DepthMax + 6
	elif tloc_bed[i]*ConcMax/DepthMax > tloc_conc[i]:
		tloc = tloc_bed[i]*ConcMax/DepthMax + 6
	else:
		tloc = tloc_conc[i] + 6
	
	# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
	if igstr[i] == 'Ignition':
		ax.text( bar_loc[i], tloc, '\u26A1', c='r', horizontalalignment='center', size = 16)
	elif igstr[i] == 'No':
		ax.text(bar_loc[i], tloc, '\u2744', c='c', horizontalalignment='center', size = 16)
	elif igstr[i] == 'Ignition without Propagation':
		ax.text(bar_loc[i], tloc, '\u26A1  ', c='r', horizontalalignment='center', size = 16)
		ax.text(bar_loc[i], tloc, '  \u2744', c='c', horizontalalignment='center', size = 16)
	else:
		ax.text(bar_loc[i], tloc, '????', c='r', horizontalalignment='center', size = 16)
		print(igstr[i])

if figtitles == 1:
	plt.title('Soil Contaminant Composition and GAC Bed Depth')

plt.savefig(figrootname + 'ContaminantComparison.png')

#######################################
# Plot concentration bar chart with GAC bed depth in separate subplot
#######################################
#  Create figure with two axes
plt.figure(figi)
figi += 1

plt.subplots_adjust(hspace = 0.27)

GACColor = CUclrs[0]
PetrolColor = CUclrs[1]
GACBedColor = CUclrs[2]

plt.subplot(2,1,1)
# Create Legend
plt.bar(0, 0, color=GACColor)
plt.bar(0, 0, color=PetrolColor)
plt.bar(0, 0, color=GACBedColor)
plt.bar(0, 0, color='w', edgecolor='k')
plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$') # Snowflake
plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$') # Thunderbolt
plt.legend( ['No Ignition', 'Ignition', 'Concentration GAC', 'Concentration Petroleum', 'GAC Bed Depth', 'Clean Cap Depth'])

# x-axis values for histogram plot
bar_loc = np.arange(0, enumf) 
b_width = 0.5

plt.subplot(2,1,1)
# Plot contaminant concentration with crude oil in separate color than GAC
for i in range(0, enumf):
	if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
		plt.bar(bar_loc[i], conc[i], color=PetrolColor, width=b_width,)
	else:
		plt.bar(bar_loc[i], conc[i], color=GACColor, width=b_width,)

# Plot parameters  
# plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
plt.xticks(bar_loc, expID)
plt.xlabel('Experiment ID')
plt.ylabel('Concentration [g/kg]')
ConcMax = max(conc)+ 40 # Concentration max y value
plt.ylim(0, ConcMax)

if figtitles == 1:
	plt.title('Initial Contaminant Composition and GAC Bed Depth')

# Plot text
tloc_conc = np.array(conc) + 2 # Top of concentration bar

for i in range(0, enumf):
	# Concentration Bar
	plt.text(bar_loc[i], tloc_conc[i], conc[i], horizontalalignment='center')
	
	tloc = tloc_conc[i] + 12
	
	# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
	if igstr[i] == 'Ignition':
		plt.text( bar_loc[i], tloc, '\u26A1', c='r', horizontalalignment='center', size = 16)
	elif igstr[i] == 'No':
		plt.text(bar_loc[i], tloc, '\u2744', c='c', horizontalalignment='center', size = 16)
	elif igstr[i] == 'Ignition without Propagation':
		plt.text(bar_loc[i], tloc, '\u26A1', c='r', horizontalalignment='center', size = 16)
		plt.text(bar_loc[i], tloc + 12, '\u2744', c='c', horizontalalignment='center', size = 16)
	else:
		plt.text(bar_loc[i], tloc, '????', c='r', horizontalalignment='center', size = 16)
		print(igstr[i])


plt.subplot(2,1,2)
bwidth = 0.4
# Plot GAC depth and Clean Cap Depth
Achannel = 329 # Cross sectional area of a single channnel (cm2)
GACdepth = np.array(GACbed)/Achannel
CapDepth = np.array(CleanCap)/Achannel
DepthMax = 2.3 # Max value for y axis for depths

for i in range(0, len(bar_loc)):
	if CapDepth[i] == 0:
		plt.bar(bar_loc[i], GACdepth[i], color=GACBedColor, width=b_width)
	else:
		plt.bar(bar_loc[i] - b_width/2, GACdepth[i], color=GACBedColor, width=b_width)
		plt.bar(bar_loc[i] + b_width/2, CapDepth[i], color='w', edgecolor = 'k', width=b_width)

# Right vertical axis parameters
plt.ylabel('GAC Bed Depth [cm]')
plt.ylim(0, DepthMax)
plt.xticks(bar_loc, expID)
plt.xlabel('Experiment ID')

# Plot text
tloc_bed = GACdepth* 1.01 # Top of GAC depth bar
tloc_cap = CapDepth*1.01 # Top of Cap depth bar
	
# Plot labels on top of each bar
for i in range(0, enumf):
	
	# GAC depth bar
	if GACdepth[i] == 0:
		GACstr = ''
	elif CapDepth[i] > 0:
		GACstr = '%0.1f  ' % GACdepth[i]
	else:
		GACstr = '%0.1f' % GACdepth[i]
	
	Capstr = ' %0.1f' % CapDepth[i]

	if CapDepth[i] == 0:
		plt.text(bar_loc[i], tloc_bed[i], GACstr, horizontalalignment='center')
	else:
		plt.text(bar_loc[i] - b_width/2, tloc_bed[i], GACstr, horizontalalignment='center')
		plt.text(bar_loc[i] + b_width/2, tloc_cap[i], Capstr, horizontalalignment='center')


	# Determine vertical location for snowflakes
	if GACdepth[i] == GACdepth[0]:
		tloc = 0
	elif CapDepth[i] == 0:
		tloc = tloc_bed[i] + 0.12
	else:
		tloc = tloc_cap[i] + 0.12
	
	# Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
	if igstr[i] == 'Ignition':
		plt.text( bar_loc[i], tloc, '\u26A1', c='r', horizontalalignment='center', size = 16)
	elif igstr[i] == 'No':
		plt.text(bar_loc[i], tloc, '\u2744', c='c', horizontalalignment='center', size = 16)
	elif igstr[i] == 'Ignition without Propagation':
		plt.text(bar_loc[i], tloc, '\u26A1', c='r', horizontalalignment='center', size = 16)
		plt.text(bar_loc[i], tloc + 0.12, '\u2744', c='c', horizontalalignment='center', size = 16)
	else:
		plt.text(bar_loc[i], tloc, '????', c='r', horizontalalignment='center', size = 16)
		print(igstr[i])



plt.savefig(figrootname + 'ContaminantComparison2.png')

plt.show()