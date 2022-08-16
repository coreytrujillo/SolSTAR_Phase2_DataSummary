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
# mpl.rcParams["figure.figsize"] = (12, 6.75)
# mpl.rcParams['font.size'] = 15
# figrootname = './Figures/' + datetime.now().strftime('%y%m%d') + '_' # Figure Output name root
figrootname = './Figures/' # Figure Output name root
figi = 1 # Initiate igure iterator
figtitles = 0 # Include titles on figures



# Set up figure
# plt.figure(figi)
# figi += 1
fig, ax = plt.subplots()

ax2 = ax.twinx() # create seocnd y axis

# Create Legend
plt.bar(0, 0, color=CUclrs[0])
plt.bar(0, 0, color=CUclrs[1])
plt.bar(0, 0, color=CUclrs[2])
plt.bar(0, 0, color='w', edgecolor='k')
plt.scatter(None, None, 150, c='c', linewidths=0.05, marker=u'$\u2744$') # Snowflake
plt.scatter(None, None, 150, c='r', linewidths=0.1, marker=u'$\u26A1$') # Thunderbolt
plt.legend( ['No Ignition', 'Ignition', 'Concentration GAC', 'Concentration Petroleum', 'GAC Bed Depth'])

# x-axis values for histogram plot
bar_loc = np.arange(0, enumf) 

for i in range(0, enumf):
    if ('Road Mix'  in elbl[i]) or ('Crude Oil' in elbl[i]):
        ax.bar(bar_loc[i], conc[i], color=CUclrs[1], width=0.25,)
    else:
        ax.bar(bar_loc[i], conc[i], color=CUclrs[0], width=0.25,)
    
ax.set_xticks(bar_loc, expID)
ax.set_xlabel('Experiment ID')
ax.set_ylabel('Concentration [g/kg]')
ax.set_ylim(0, max(conc)+ 25)
ax.spines['left'].set_color(CUclrs[0])
ax.yaxis.label.set_color(CUclrs[0])
ax.tick_params(axis='y', colors=CUclrs[0])

GACdepth = np.array(GACbed)/329
CapDepth = np.array(CleanCap)/329
ax2.bar(bar_loc - 0.25, GACdepth, color=CUclrs[2], width=0.25)
ax2.bar(bar_loc + 0.25, CapDepth, color='w', edgecolor = 'k', width=0.25)
ax2.set_ylabel('GAC Bed depth [cm]')
ax2.set_ylim(0, 3)
ax2.spines['right'].set_color(CUclrs[2])
ax2.yaxis.label.set_color(CUclrs[2])
ax2.tick_params(axis='y', colors=CUclrs[2])

tloc_conc = np.array(conc) + 2
tloc_bed = GACdepth* 1.01
tloc_cap = CapDepth*1.01
for i in range(0, enumf):
    ax.text(bar_loc[i], tloc_conc[i], conc[i], horizontalalignment='center')
    if GACdepth[i] == 0:
        GACstr = str(0)
    else:
        GACstr = ' %0.1f' % GACdepth[i]
    
    if CapDepth[i] == 0:
        Capstr = str(0)
    else:
        Capstr = ' %0.1f' % CapDepth[i]
    ax2.text(bar_loc[i] - 0.25, tloc_bed[i], GACstr, horizontalalignment='center')
    ax2.text(bar_loc[i] + 0.25, tloc_cap[i], Capstr, horizontalalignment='center')

    # Determine vertical location for snowflakes
    if tloc_cap[i]*225/3 >  tloc_conc[i]:
        tloc = tloc_cap[i]*225/3 + 8
    elif tloc_bed[i]*225/3 > tloc_conc[i]:
        tloc = tloc_bed[i]*225/3 + 8
    else:
        tloc = tloc_conc[i] + 8
    
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

if figtitles == 1:
    plt.title('Soil Contaminant Composition and GAC Bed Depth')

plt.savefig(figrootname + 'ContaminantComparison.png')

plt.show()