# Set up unique markers for Collectors and Fibers
Cstr = ['C1', 'C2', 'C3', 'C4']
Fstr = ['FA', 'FB', 'FC', 'FD', 'FE', 'FF', 'FG', 'FH']

# File names for experiment data
efpath = 'c:/Users/corey/OneDrive - UCB-O365/CU/Linden/Experiments/Box_Concept//Box_Experiments/'

e220515 = '220515_SingleChannel_GACSoil/220515_SingleChannel_GACSoil_data.csv'
e220602 = '220602_SingleChannel_GACSoil/220602_SingleChannel_GACSoil_data.csv'
e220604 = '220604_SingleChannel_GACSoil/220604_SingleChannel_GACSoil_data.csv'
e220608 = '220608_SingleChannel_GACSoil/220608_SingleChannel_GACSoil_data.csv'
e220610 = '220610_SingleChannel_GACSoil_GACBase/220610_SingleChannel_GACSoil_GACBase_data_COMBINED.csv'
e220611 = '220611_SingleChannel_GACSoil_GACBase/220611_SingleChannel_GACSoil_GACBase_data.csv'
e220613 = '220613_SingleChannel_GACSoilAndBase/220613_SingleChannel_GACSoilAndBase_data.csv'
e220617 = '220617_DrillCuttings/220617_DrillCuttings_data.csv'
e220623 = '220623_GACSoil4percent_GACBase/220623_GACSoil4percent_GACBase_data.csv'
e220628 = '220628_GACSoil6Percent_GACBase/220628_GACSoil6Percent_GACBase_data.csv'
e220708 = '220708_AquariumGACSoil5Percent_GACBase/220708_AquariumGACSoil5Percent_GACBase_data.csv'
e220712 = '220712_PoolSandGAC4Percent_GACBase/220712_PoolSandGAC4Percent_GACBase_data.csv'
e220717 = '220717_PoolSand4PercentGAC_450mLGACBase/220717_PoolSand4PercentGAC_450mLGACBase_data.csv'
e220719 = '220719_PoolSand4PercentGAC_450mLGACBase/220719_PoolSand4PercentGAC_450mLGACBase_data.csv'
e220720 = '220720_PoolSand4PercentGAC_450mLGACBase/220720_PoolSand4PercentGAC_450mLGACBase_data.csv'
e220730 = '220730_PoolSand4PercentGAC_450mLGACBase/220730_PoolSand4PercentGAC_450mLGACBase_data.csv'
e220804 = '220804_PoolSand4Percent GAC_300mLGACBase_CleanCap/220804_PoolSand4Percent GAC_300mLGACBase_CleanCap_data.csv'
e220809 = '220809_CrudeOil_PoolSand/220809_CrudeOil_PoolSand_data.csv'
e220810 = '220810_CrudeOil_PoolSand/220810_CrudeOil_PoolSand_data.csv'
e220812 = '220812_PoolSand4PercentGAC_450mLGACBase_CleanCap/220812_PoolSand4PercentGAC_450mLGACBase_CleanCap_data.csv'
e220926 = '220926_CrudeOil_PoolSand_5Percent/220926_CrudeOil_PoolSand_5Percent_data.csv'
e221010 = '221010_HiRezTC/221010_HiRezTC_data.csv'
e221013 = '221013_HiRezTC/221013_HiRezTC_data.csv'
e221018 = '221018_HiRez_Quartz/221018_HiRez_Quartz_data.csv'

enames = [e220515, e220602, e220604, e220608, e220610, e220611, e220613, e220617, e220623, e220628, e220708, e220712, e220717, e220719, e220720, e220730, e220804, e220809, e220810, e220812, e220926, e221010, e221013, e221018]

edatestrs = ['220515', '220602', '220604', '220608',  '220610', '220611', '220613', '220617', '220623', '220628', '220708', '220712', '220717', '220719', '220720', '220730', '220804', '220809', '220810', '220812', '220926', '221010', '221013', '221018' ]

# Experiment label
elbl220515 = ['GAC Soil 20 g/kg']
elbl220602 = ['GAC Soil 200 g/kg']
elbl220604 = ['GAC Soil 200 g/kg']
elbl220608 = ['GAC Soil 200 g/kg: 3 Collectors', 'GAC Soil 200 g/kg: 4 Collectors']
elbl220610 = ['GAC Soil 200 g/kg on 600 mL GAC bed']
elbl220611 = ['GAC Soil 200 g/kg on a 600 mL GAC bed']
elbl220613 = ['GAC Soil 200 g/kg on a 300 mL GAC bed', 'GAC Soil 200 g/kg on a 300 mL GAC bed']
elbl220617 = ['Road Mix on bed of GAC']
elbl220623 = ['GAC Soil 40 g/kg on a 300 mL GAC bed']
elbl220628 = ['GAC Soil 60 g/kg on a 600 mL GAC bed']
elbl220708 = ['GAC Aquarium Sand 50 g/kg on 600 mL GAC bed']
elbl220712 = ['GAC Pool Sand 40 g/kg on a 600 mL GAC bed']
elbl220717 = ['GAC Pool Sand 40 g/kg on a 450 mL GAC bed']
elbl220719 = ['GAC Pool Sand 40 g/kg on a 450 mL GAC bed']
elbl220720 = ['GAC Pool Sand 40 g/kg on a 450 mL GAC bed']
elbl220730 = ['GAC Pool Sand 40 g/kg on a 450 mL GAC bed']
elbl220804 = ['GAC Pool Sand 40 g/kg on a 450 mL GAC bed with Clean Soil Cap']
elbl220809 = ['Crude Oil Soil 27 g/kg on a 300 mL GAC bed']
elbl220810 = ['Crude Oil Soil 27 g/kg on a 300 mL GAC bed', 'Crude Oil Soil 27 g/kg on 300 mL GAC bed Reheat']
elbl220812 = ['GAC Soil 40 g/kg on 450 mL GAC bed with Clean Cap']
elbl220926 = ['Crude Oil Soil 50g/kg on a 450 mL GAC bbed']
elbl221010 = ['High Resolution TCs GAC Soil 40 g/kg on a 450 mL GAC bed']
elbl221013 = ['High Resolution TCs GAC Soil 40 g/kg on a 450 mL GAC bed']
elbl221018 = ['High Rez TCs GAC Soil 40 g/kg on a 450 mL GAC bed with Quartz TR']

elbl = elbl220515 + elbl220602 + elbl220604 + elbl220608 + elbl220610 + elbl220611 +  elbl220613 + elbl220617 + elbl220623 + elbl220628 + elbl220708 + elbl220712 + elbl220717 + elbl220719 + elbl220720 + elbl220730 + elbl220804 + elbl220809 + elbl220810 + elbl220812 + elbl220926 + elbl221010 + elbl221013 + elbl221018

elblidx = [elbl220515, elbl220602, elbl220604, elbl220608,  elbl220610, elbl220611, elbl220613, elbl220617, elbl220623, elbl220628, elbl220708, elbl220712, elbl220717, elbl220719, elbl220720, elbl220730, elbl220804, elbl220809, elbl220810, elbl220812, elbl220926, elbl221010, elbl221013, elbl221018 ]


# Experiment Identifier
expID220515 = ['A']
expID220602 = ['B']
expID220604 = ['C']
expID220608 = ['D', 'E']
expID220610 = ['F']
expID220611 = ['G']
expID220613 = ['H', 'I']
expID220617 = ['J']
expID220623 = ['K']
expID220628 = ['L']
expID220708 = ['M']
expID220712 = ['N']
expID220717 = ['O']
expID220719 = ['P']
expID220720 = ['Q']
expID220730 = ['R']
expID220804 = ['S']
expID220809 = ['T']
expID220810 = ['U', 'V']
expID220812 = ['W']
expID220926 = ['X']
expID221010 = ['Y']
expID221013 = ['Z']
expID221018 = [r'$\alpha$']


expID = expID220515 + expID220602 + expID220604 + expID220608 + expID220610 + expID220611 +  expID220613 + expID220617 + expID220623 + expID220628 + expID220708 + expID220712 + expID220717 + expID220719 + expID220720 + expID220730 + expID220804 + expID220809 + expID220810 + expID220812 + expID220926 + expID221010 + expID221013 + expID221018

# Collector/Fiber Pairs in use for each experiment
cf220517 = ['C1FC, C2FA, C3FF']
cf220602 = ['C1FC, C2FA, C3FF']
cf220604 = ['C1FC, C3FF, C4FD']
cf220608 = ['C1FC, C2FA, C3FF', 'All Four']
cf220610 = ['All Four']
cf220611 = ['All Four']
cf220613 = ['C1FC, C2FA, C3FF', 'All Four']
cf220617 = ['All Four']
cf220623 = ['All Four']
cf220628 = ['All Four']
cf220708 = ['All Four']
cf220712 = ['All Four']
cf220717 = ['All Four']
cf220719 = ['All Four']
cf220720 = ['All Four']
cf220730 = ['All Four']
cf220804 = ['All Four']
cf220809 = ['All Four']
cf220810 = ['All Four', 'All Four']
cf220812 = ['All Four']
cf220926 = ['All Four']
cf221010 = ['All Four']
cf221013 = ['All Four']
cf221018 = ['All Four']


cfstr = cf220517 + cf220602 + cf220604 + cf220608 + cf220610 + cf220611 + cf220613 + cf220617 + cf220623 + cf220628 + cf220708 + cf220712 + cf220717 + cf220719 + cf220720 + cf220730 + cf220804 + cf220809 + cf220810 + cf220812 + cf220926 + cf221010 + cf221013 + cf221018

# Time power on
etistr220515 = ['16:14:00']
etistr220602 = ['14:08:00']
etistr220604 = ['12:10:00']
etistr220608 = ['11:12:00', '15:02:00']
etistr220610 = ['11:34:00']
etistr220611 = ['11:00:00']
etistr220613 = ['11:12:00', '12:23:00']
etistr220617 = ['10:45:00']
etistr220623 = ['11:56:00']
etistr220628 = ['11:12:00']
etistr220708 = ['11:18:00']
etistr220712 = ['12:25:00']
etistr220717 = ['10:41:00']
etistr220719 = ['10:37:00']
etistr220720 = ['10:38:00']
etistr220730 = ['9:37:00']
etistr220804 = ['11:17:00']
etistr220809 = ['12:07:00']
etistr220810 = ['11:57:00', '11:57:00']
etistr220812 = ['11:13:00']
etistr220926 = ['11:12:00']
etistr221010 = ['11:50:00']
etistr221013 = ['10:03:00']
etistr221018 = ['10:46:00']

etistr = etistr220515 + etistr220602 + etistr220604 + etistr220608 + etistr220610 + etistr220611 + etistr220613 + etistr220617 + etistr220623 + etistr220628 + etistr220708 + etistr220712 + etistr220717 + etistr220719 + etistr220720 + etistr220730 + etistr220804 + etistr220809 + etistr220810 + etistr220812 + etistr220926 + etistr221010 + etistr221013 + etistr221018

# Time power off
etfstr220515 = ['17:32:00']
etfstr220602 = ['16:55:00']
etfstr220604 = ['13:35:00']
etfstr220608 = ['14:35:00', '16:34:00']
etfstr220610 = ['13:47:00']
etfstr220611 = ['13:07:00']
etfstr220613 = ['11:45:00', '15:46:00']
etfstr220617 = ['13:47:00']
etfstr220623 = ['16:21:00']
etfstr220628 = ['15:10:00']
etfstr220708 = ['14:19:00']
etfstr220712 = ['14:18:00']
etfstr220717 = ['14:34:00']
etfstr220719 = ['12:40:00']
etfstr220720 = ['11:55:00']
etfstr220730 = ['12:35:00']
etfstr220804 = ['15:07:00']
etfstr220809 = ['14:10:00']
etfstr220810 = ['13:44:00', '15:00:00']
etfstr220812 = ['13:58:00']
etfstr220926 = ['13:40:00']
etfstr221010 = ['14:08:00']
etfstr221013 = ['14:15:00']
etfstr221018 = ['13:55:00']

etfstr = etfstr220515 + etfstr220602 + etfstr220604 + etfstr220608 + etfstr220610 + etfstr220611 + etfstr220613 + etfstr220617 + etfstr220623 + etfstr220628 + etfstr220708 + etfstr220712 + etfstr220717 + etfstr220719 + etfstr220720 + etfstr220730 + etfstr220804 + etfstr220809 + etfstr220810 + etfstr220812 + etfstr220926 + etfstr221010 + etfstr221013 + etfstr221018

# Aeration time strings
AirT220515 = ['17:21:00']
AirT220602 = ['16:44:00']
AirT220604 = ['X']
AirT220608 = ['13:01:00', '16:12:00']
AirT220610 = ['X']
AirT220611 = ['12:57:00']
AirT220613 = ['X', '14:44:00']
AirT220617 = ['13:35:00']
AirT220623 = ['14:55:00']
AirT220628 = ['14:48:00']
AirT220708 = ['14:02:00']
AirT220712 = ['14:00:00']
AirT220717 = ['14:14:00']
AirT220719 = ['12:33:00']
AirT220720 = ['X']
AirT220730 = ['12:07:00']
AirT220804 = ['14:19:00']
AirT220809 = ['13:59:00']
AirT220910 = ['13:33:00', '14:21:00']
AirT220812 = ['13:26:00']
AirT220926 = ['13:26:00']
AirT221010 = ['13:55:00']
AirT221013 = ['13:54:00']
AirT221018 = ['13:27:00']

AirT = AirT220515 + AirT220602 + AirT220604 + AirT220608 + AirT220610 + AirT220611 + AirT220613 + AirT220617 + AirT220623 + AirT220628 + AirT220708 + AirT220712 + AirT220717 + AirT220719 + AirT220720 + AirT220730 + AirT220804 + AirT220809 + AirT220910 + AirT220812 + AirT220926 + AirT221010 + AirT221013 + AirT221018

# Initial temperature filter strings
Tempi220515 = [0]
Tempi220602 = [0]
Tempi220604 = [0]
Tempi220608 = [0, 0]
Tempi220610 = [0]
Tempi220611 = [0]
Tempi220613 = [0, 0]
Tempi220617 = [0]
Tempi220623 = [0]
Tempi220628 = [0]
Tempi220708 = ['13:02:00']
Tempi220712 = [0]
Tempi220717 = [0]
Tempi220719 = [0]
Tempi220720 = [0]
Tempi220730 = [0]
Tempi220804 = [0]
Tempi220809 = [0]
Tempi220810 = [0, 0]
Tempi220812 = [0]
Tempi220926 = [0]
Tempi221010 = [0]
Tempi221013 = [0]
Tempi221018 = [0]

Tempi = Tempi220515 + Tempi220602  + Tempi220604 + Tempi220608 + Tempi220610 + Tempi220611 + Tempi220613 + Tempi220617 + Tempi220623 + Tempi220628 + Tempi220708 + Tempi220712 + Tempi220717 + Tempi220719 + Tempi220720 + Tempi220730 + Tempi220804 + Tempi220809 + Tempi220810 + Tempi220812 + Tempi220926 + Tempi221010 + Tempi221013 + Tempi221018


# Final temperature filter strings
Tempf220515 = ['17:55:00']
Tempf220602 = [0]
Tempf220604 = [0]
Tempf220608 = [0, 0]
Tempf220610 = [0]
Tempf220611 = [0]
Tempf220613 = ['11:45:00', 0]
Tempf220617 = [0]
Tempf220623 = ['17:00:00']
Tempf220628 = [0]
Tempf220708 = [0]
Tempf220712 = [0]
Tempf220717 = [0]
Tempf220719 = [0]
Tempf220720 = [0]
Tempf220730 = [0]
Tempf220804 = [0]
Tempf220809 = [0]
Tempf220810 = [0, 0]
Tempf220812 = ['16:25:00']
Tempf220926 = [0]
Tempf221010 = [0]
Tempf221013 = [0]
Tempf221018 = [0]

Tempf = Tempf220515 + Tempf220602 + Tempf220604 + Tempf220608 + Tempf220610 + Tempf220611 + Tempf220613 + Tempf220617 + Tempf220623 + Tempf220628 + Tempf220708 + Tempf220712 + Tempf220717 + Tempf220719 + Tempf220720 + Tempf220730 + Tempf220804 + Tempf220809 + Tempf220810 + Tempf220812 + Tempf220926 + Tempf221010 + Tempf221013 + Tempf221018

# Ignition string
ig220517 = ['No']
ig220602 = ['No']
ig220604 = ['No']
ig220608 = ['No', 'No']
ig220610 = ['No']
ig220611 = ['Ignition']
ig220613 = ['No', 'Ignition']
ig220617 = ['Ignition']
ig220623 = ['No']
ig220628 = ['Ignition without Propagation'] 
ig220708 = ['Ignition']
ig220712 = ['Ignition']
ig220717 = ['Ignition']
ig220719 = ['No']
ig220720 = ['No']
ig220730 = ['Ignition']
ig220804 = ['Ignition without Propagation']
ig220809 = ['No']
ig220810 = ['No', 'No']
ig220812 = ['Ignition without Propagation']
ig220926 = ['Ignition without Propagation']
ig221010 = ['Ignition without Propagation']
ig221013 = ['Ignition']
ig221018 = ['Ignition without Propagation']

igstr = ig220517 + ig220602 + ig220604 + ig220608 + ig220610 + ig220611 + ig220613 + ig220617 + ig220623 + ig220628 + ig220708 + ig220712 + ig220717 + ig220719 + ig220720 + ig220730 + ig220804 + ig220809 + ig220810 + ig220812 + ig220926 + ig221010 + ig221013 + ig221018

# Contamination concentrations [g/kg]
conc220517 = [20]
conc220602 = [200]
conc220604 = [200]
conc220608 = [200, 200]
conc220610 = [200]
conc220611 = [200]
conc220613 = [200, 200]
conc220617 = [27]
conc220623 = [40]
conc220628 = [63] 
conc220708 = [50]
conc220712 = [40]
conc220717 = [40]
conc220719 = [40]
conc220720 = [40]
conc220730 = [40]
conc220804 = [40]
conc220809 = [27]
conc220810 = [27, 27]
conc220812 = [40]
conc220926 = [50]
conc221010 = [40]
conc221013 = [40]
conc221018 = [40]

conc = conc220517 + conc220602 + conc220604 + conc220608 + conc220610 + conc220611 + conc220613 + conc220617 + conc220623 + conc220628 + conc220708 + conc220712 + conc220717 + conc220719 + conc220720 + conc220730 + conc220804 + conc220809 + conc220810 + conc220812 + conc220926 + conc221010 + conc221013 + conc221018

# GAC Bed Volume [mL]
GACbed220517 = [0]
GACbed220602 = [0]
GACbed220604 = [0]
GACbed220608 = [0, 0]
GACbed220610 = [600]
GACbed220611 = [600]
GACbed220613 = [600, 600]
GACbed220617 = [300]
GACbed220623 = [300]
GACbed220628 = [600] 
GACbed220708 = [600]
GACbed220712 = [600]
GACbed220717 = [450]
GACbed220719 = [450]
GACbed220720 = [450]
GACbed220730 = [450]
GACbed220804 = [300]
GACbed220809 = [300]
GACbed220810 = [300, 300]
GACbed220812 = [450]
GACbed220928 = [450]
GACbed221010 = [450]
GACbed221013 = [450]
GACbed221018 = [450]

GACbed = GACbed220517 + GACbed220602 + GACbed220604 + GACbed220608 + GACbed220610 + GACbed220611 + GACbed220613 + GACbed220617 + GACbed220623 + GACbed220628 + GACbed220708 + GACbed220712 + GACbed220717 + GACbed220719 + GACbed220720 + GACbed220730 + GACbed220804 + GACbed220809 + GACbed220810 + GACbed220812 + GACbed220928 + GACbed221010 + GACbed221013 + GACbed221018

# Clean Cap volume
CleanCap220515 = [0]
CleanCap220602 = [0]
CleanCap220604 = [0]
CleanCap220608 = [0, 0]
CleanCap220610 = [0]
CleanCap220611 = [0]
CleanCap220613 = [0, 0]
CleanCap220617 = [0]
CleanCap220623 = [0]
CleanCap220628 = [0]
CleanCap220708 = [0]
CleanCap220712 = [0]
CleanCap220717 = [0]
CleanCap220719 = [0]
CleanCap220720 = [0]
CleanCap220730 = [0]
CleanCap220804 = [500]
CleanCap220809 = [0]
CleanCap220810 = [0, 0]
CleanCap220812 = [500]
CleanCap220926 = [0]
CleanCap221010 = [0]
CleanCap221013 = [0]
CleanCap221018 = [0]

CleanCap = CleanCap220515 + CleanCap220602 + CleanCap220604 + CleanCap220608 + CleanCap220610 + CleanCap220611 + CleanCap220613 + CleanCap220617 + CleanCap220623 + CleanCap220628 + CleanCap220708 + CleanCap220712 + CleanCap220717 + CleanCap220719 + CleanCap220720 + CleanCap220730 + CleanCap220804 + CleanCap220809 + CleanCap220810 + CleanCap220812 + CleanCap220926 + CleanCap221010 + CleanCap221013 + CleanCap221018

