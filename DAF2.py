import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import numpy as np
import pysine
import time

def defcolors(numf):
	# Setup plot colors
	CUGold = '#CFB87C'
	CUdarkgrey = '#565A5C'
	CUlightgrey= '#A2A4A3'
	UNRBlue = '#003366'
	UNRsilver = '#D4D3D6'
	UPPurple = '#1E1656'
	UPGrey = '#5E6A71'

	clrs = ['red', 'darkorange', 'gold', 'green','blue', 'purple', 'magenta', 'gray', 'darkred', 'coral', 'yellow',  'lime', 'cornflowerblue', 'peru', 'brown', 'firebrick', 'chocolate', 'yellowgreen', 'cyan', 'slateblue', 'deeppink', 'darksalmon' , 'darkseagreen', 'darkturquoise', 'darkorchid', 'fuchsia', 'orange', 'goldenrod',  'forestgreen', 'dodgerblue', 'mediumblue', 'mediumorchid', 'indigo', 'maroon', 'salmon','chartreuse', 'deepskyblue', 'darkviolet', 'crimson', 'darkgoldenrod', 'greenyellow', 'limegreen', 'navy', 'rebeccapurple', 'grey' ]

	CUclrs = [CUGold, CUdarkgrey, CUlightgrey, 'black']
	UNRclrs = [UNRBlue, UNRsilver]
	UPclrs = [UPPurple, 'white', UPGrey]

	# If there aren't enough color options for the dataset, show remaining options
	if numf > len(clrs):
		# Notify user that there aren't enough colors named
		print('You need to add some colors \n')
		print('Consider the following: \n')
		
		# Identify remaning colors and plot for user
		poscols = [] # Initiate possible color variable
		for name, hex in mpl.colors.cnames.items():
			poscols.append(name)
		for x in set(poscols).intersection(clrs):
			poscols.remove(x)
		print(poscols)
		
		# Tell user how many colors are needed
		print('\nThere are only',  len(clrs), 'but', numf ,'datasets to plot')
		print('You need to add', numf - len(clrs),  'colors')
		print('Consider colors above')
		
		# Plot available colors
		mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color = poscols)
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ratio = 1.0 / 3.0
		count = np.ceil(np.sqrt(len(poscols)))
		x_count = count * ratio
		y_count = count / ratio
		x = 0
		y = 0
		w = 1 / x_count
		h = 1 / y_count
		for c in poscols:
			pos = (x / x_count, y / y_count)
			ax.add_patch(mpl.patches.Rectangle(pos, w, h, color=c))
			ax.annotate(c, xy=pos)
			if y >= y_count-1:
				x += 1
				y = 0
			else:
				y += 1

		plt.show()
		exit()
		
	else:
		return clrs, CUclrs#, UNRclrs, UPclrs

def makemarker(lbl, Cstr, Fstr, clrs):
	# This function creates a unique marker for each collector defined in Cstr and a unique color for each fiber defined in Fstr
	# lbl should be the label string which contains the fiber and collector labels
	# clrs should be colors defined in the defcolors function
	# mkrs = marker shape
	# mkrc = marker color
	
	mkrs = []
	mkrc = []
	
	# Define marker shapes
	ms = ['o', '^', 's', 'x']
	
	# Ensure there are enough marker shapes for defined collectors
	if len(Cstr) > len(ms):
		print('There are only ', len(ms), 'marker shapes defined')
		print('But', len(Cstr), 'Collectors defined')
		print('You need to add some marker shapes')
		exit()
	
	# Ensure there are enough colors for fibers
	if len(Fstr) > len(clrs):
		print('There are only ', len(clrs), 'colors defined')
		print('But', len(Fstr), 'fibers defined')
		print('You need to add more colors')
		exit()
	
	# Identify marker shape for each collector
	for i in range(0, len(lbl)):
		for j in range(0, len(Cstr)):
			if Cstr[j] in lbl[i]:
				mkrs.append(ms[j])
	
	# Identify marker color for each fiber
	for i in range(0, len(Fstr)):
		for j in range(0, len(Fstr)):
			if Fstr[j] in lbl[i]:
				mkrc.append(clrs[j])
	
	return mkrs, mkrc

def data_filter(data, datestr, tistr, tfstr):
	# This script filters data for a particular timeset
	# fpath = path to file string including file name
	# datestr = six-digit date string YYMMDD
	# tistr = filter start time string HH:MM:SS. Enter 0 to start filter at beginning of data colleciton
	# tfstr = filter finish time string HH:MM:SS. Enter 0 to start filter at beginning of data colleciton
	# lbl = label for this filtered dataset
	# hvar = string for header of data being filtered

	if tistr == 0:
		dti = data['Time'][0]
	else:
		dti = datetime.strptime(datestr + ' ' + tistr, '%y%m%d %H:%M:%S')

	if tfstr == 0:
		dtf = data['Time'][data.index.max()]
	else:
		dtf = datetime.strptime(datestr + ' ' + tfstr, '%y%m%d %H:%M:%S')

	# Filter data
	filt = (data['Time'] >= dti) & (data['Time'] <= dtf) 
	dataf = data.loc[filt]
	
	# Create Run Time variable in minuntes
	dRT = (dataf['Time'] - dataf['Time'][dataf.index.min()]).dt.total_seconds()/60
	dataf = dataf.assign(RunTime = dRT)
	# dataf['RunTime'] = (dataf['Time'] - dataf['Time'][dataf.index.min()]).dt.total_seconds()/60

	dataf = dataf.reset_index()
		
	return dataf

def data_read_format(fpath, datestr):
	data = pd.read_csv(fpath, header = 0)
	data['Time'] = pd.to_datetime(datestr + ' ' + data['Time'], format='%y%m%d %H:%M:%S.%f')
	
	return data

def rsquared(x, y, C0, C1):
    # This function solves the R-squared value for data
    # AKA the coefficient of determination
    # x is the x-coordinate of the data
    # y is the y-coordinate of the data
    # C0 is the slope of the trendline
    # C1 is the intercept of the trendline
    SSR = sum((y - (C0*x + C1))**2) # Residual sum of squares
    SST = sum((y - y.mean())**2) # Total sum of squares
    R2 = 1 - SSR/SST

    return R2

# Linear Regression	
def linreg(x, y, tx, ty, p=True):
	# This script takes data and performs a linear regression. It outputs the trendline and R-Squared value. 
	# See notes from Murty's ME Analysis from 10/10 for how this was developed
	# p is True plot and False for no plot
	# S = C*V
	
	x = np.asarray(x)
	y = np.asarray(y)
	
	# Vandermonde? Matrix
	V = np.array([[len(x), sum(x)], [sum(x), sum(x*x)]]) 
	S = np.array([[sum(y)], [sum(x*y)]])
	
	# Coefficients of tendline
	C = np.linalg.solve(V, S)
	C = np.flip(C)
	
	# Evaluate Trendline at Coefficients
	TLx = np.sort(x)
	TLy = np.polyval(C, TLx)
	
	# Calculate R-squared value
	R2 = rsquared(x, y, C[0], C[1])
	
	if p:
		# Text locations and content
		if tx == 0:
			txo = TLx[-1] - (TLx[-1] - TLx[0])*0.15
		else: txo = tx

		if ty == 0:	
			if C[0][0] > 0:
				tyo = TLy[-1]
			elif C[0][0] < 0:
				tyo = TLy[-1] + abs(TLy[-1] - TLy[0])*0.2
		else: tyo = ty
		
		tstr =  'y = ' + "{:.1f}".format(C[0][0]) + 'x + ' + "{:.1f}".format(C[1][0]) + '\nR$^2$ = ' + "{:.2f}".format(R2)
	
		plt.plot(TLx, TLy, 'k--')
		plt.text(txo, tyo, tstr, c='k')

	return C[0][0], C[1][0]

def quadreg(x, y, tx, ty, p=True):
	# This script takes data and performs a quadratic regression. It outputs the trendline and R-Squared value. 
	# See notes from Murty's ME Analysis from 10/10 for how this was developed
	# S = C*V
	
	x = np.asarray(x)
	y = np.asarray(y)
	
	# Vandermonde? Matrix
	V = np.array([[len(x), sum(x), sum(x*x)], [sum(x), sum(x*x), sum(x*x*x)], [sum(x*x), sum(x*x*x), sum(x*x*x*x)]]) 
	S = np.array([[sum(y)], [sum(x*y)], [sum(x*x*y)] ])
	
	# Coefficients of tendline
	C = np.linalg.solve(V, S)
	C = np.flip(C)
	
	# Evaluate Trendline at Coefficients
	TLx = np.sort(x)
	TLy = np.polyval(C, TLx)
	
	# Calculate R-squared value
	SSR = sum((np.polyval(C, x) - y)**2)
	SST = sum((y - np.mean(y))**2)
	R2 = 1 - SSR/SST
	
	if p:
		# Text locations and content
		if tx == 0:
			txo = TLx[-1] - (TLx[-1] - TLx[0])*0.15
		if ty == 0:	
			if C[0][0] > 0:
				tyo = TLy[-1]*0.8
			elif C[0][0] < 0:
				tyo = TLy[-1] - abs(TLy[-1] - TLy[0])*0.2
		tstr =  'y = ' + "{:.1f}".format(C[0][0]) + 'x$^2$ + ' + "{:.1f}".format(C[1][0]) + 'x + ' + "{:.1f}".format(C[2][0]) + '\nR$^2$ = ' + "{:.2f}".format(R2)

		plt.plot(TLx, TLy, 'r--')
		plt.text(txo, tyo, tstr, c='r')
	
	return C[0][0], C[1][0], C[2][0]

# Create the proper number of windows in a subplot
def subcount(WinCount):
	if WinCount < 1:
		print('Error! Nothing to Plot????')
	elif WinCount == 1:
		spx = 1
		spy = spx
	elif WinCount == 2:
		spx = 1
		spy = 2
	elif WinCount < 5:
		spx = 2
		spy = 2
	elif WinCount < 7:
		spx = 2
		spy = 3
	elif WinCount < 10:
		spx = 3
		spy = 3
	elif WinCount < 13:
		spx = 4
		spy = 3
	elif WinCount < 17:
		spx = 4
		spy = 4
	elif WinCount < 21:
		spx = 5
		spy = 4
	elif WinCount < 26:
		spx = 5
		spy = 5
	elif WinCount < 31:
		spx = 6
		spy = 5
	elif WinCount < 37:
		spx = 6
		spy = 6
	elif WinCount < 43:
		spx = 7
		spy = 6
	elif WinCount < 50:
		spx = 7
		spy = 7
	elif WinCount < 57:
		spx = 8
		spy = 7
	elif WinCount < 100:
		spx = 10
		spy = 10
	else:
		print('We need ', WinCount, 'windows')
		print('This is more windows than the subcount function is built for')
		print('please write a new scenario for WinCount')
		exit()
	
	return spx, spy

def celebrate():
	#######################################
	# Play tone to signify end of script
	#######################################
	pysine.sine(frequency=440.0, duration=0.25)
	time.sleep(0.1)
	pysine.sine(frequency=440.0, duration=0.1)
	time.sleep(0.1)
	pysine.sine(frequency=440.0, duration=0.1)
	pysine.sine(frequency=880.0, duration=1)