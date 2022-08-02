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
mpl.rcParams["figure.figsize"] = (12, 6.75)
# mpl.rcParams['font.size'] = 15
# figrootname = './Figures/' + datetime.now().strftime('%y%m%d') + '_' # Figure Output name root
figrootname = './Figures/' # Figure Output name root
figi = 1 # Initiate igure iterator



# Set up figure
# plt.figure(figi)
# figi += 1
fig, ax = plt.subplots()

ax2 = ax.twinx() # create seocnd y axis

# Create Legend
plt.bar(0, 0, color=CUclrs[0])
plt.bar(0, 0, color=CUclrs[1])
plt.bar(0, 0, color=CUclrs[2])
plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$') # Snowflake
plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$') # Thunderbolt
plt.legend( ['No Ignition', 'Ignition', 'Concentration GAC', 'Concentration Petroleum', 'GAC Bed Depth'])

# x-axis values for histogram plot
bar_loc = np.arange(0, enumf) 

for i in range(0, enumf):
    if 'Road Mix' in elbl[i]:
        ax.bar(bar_loc[i] - 0.2, conc[i], color=CUclrs[1], width=0.4,)
    else:
        ax.bar(bar_loc[i] - 0.2, conc[i], color=CUclrs[0], width=0.4,)
    
ax.set_xticks(bar_loc, expID)
ax.set_xlabel('Experiment ID')
ax.set_ylabel('Concentration [g/kg]')
ax.set_ylim(0, max(conc)+ 25)
ax.spines['left'].set_color(CUclrs[0])
ax.yaxis.label.set_color(CUclrs[0])
ax.tick_params(axis='y', colors=CUclrs[0])

GACdepth = np.array(GACbed)/329
ax2.bar(bar_loc + 0.2, GACdepth, color=CUclrs[2], width=0.4)
ax2.set_ylabel('GAC Bed depth [cm]')
ax2.set_ylim(0, 3)
ax2.spines['right'].set_color(CUclrs[2])
ax2.yaxis.label.set_color(CUclrs[2])
ax2.tick_params(axis='y', colors=CUclrs[2])

tloc_conc = np.array(conc) + 2
tloc_bed = GACdepth* 1.01
for i in range(0, enumf):
    ax.text(bar_loc[i] - 0.2, tloc_conc[i], conc[i], horizontalalignment='center')
    ax2.text(bar_loc[i] + 0.2, tloc_bed[i], ' %0.1f' % GACdepth[i], horizontalalignment='center')

    if tloc_conc[i] > tloc_bed[i]*225/3:
        tloc = tloc_conc[i] + 8
    else:
        tloc = tloc_bed[i]*225/3 + 8
    # Plot snowflake (\u2744) or thunderbolt (\u26A1) for ignition
    if igstr[i] == 'Ignition':
        ax.text( bar_loc[i], tloc, '\u26A1', c='r', horizontalalignment='center', size = 16)
    elif igstr[i] == 'No':
        ax.text(bar_loc[i], tloc, '\u2744', c='c', horizontalalignment='center', size = 16)
    elif igstr[i] == 'Ignition without Propegation':
        ax.text(bar_loc[i], tloc, '\u26A1  ', c='r', horizontalalignment='center', size = 16)
        ax.text(bar_loc[i], tloc, '  \u2744', c='c', horizontalalignment='center', size = 16)
    else:
        ax.text(bar_loc[i], tloc, '????', c='r', horizontalalignment='center', size = 16)

plt.title('Soil Contaminant Composition and GAC Bed Depth')

plt.savefig(figrootname + 'ContaminantComparison.png')

plt.show()