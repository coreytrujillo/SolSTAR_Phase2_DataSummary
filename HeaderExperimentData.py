# Set up unique markers for Collectors and Fibers
Cstr = ['C1', 'C2', 'C3', 'C4']
Fstr = ['FA', 'FB', 'FC', 'FD', 'FE', 'FF', 'FG', 'FH']

# File names for experiment data
efpath = '../../Box_Experiments/'

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

enames = [e220515, e220602, e220604, e220608, e220610, e220611, e220613, e220617, e220623, e220628, e220708, e220712, e220717, e220719, e220720]

edatestrs = ['220515', '220602', '220604', '220608',  '220610', '220611', '220613', '220617', '220623', '220628', '220708', '220712', '220717', '220719', '220720']

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

elbl = elbl220515 + elbl220602 + elbl220604 + elbl220608 + elbl220610 + elbl220611 +  elbl220613 + elbl220617 + elbl220623 + elbl220628 + elbl220708 + elbl220712 + elbl220717 + elbl220719 + elbl220720

elblidx = [elbl220515, elbl220602, elbl220604, elbl220608,  elbl220610, elbl220611, elbl220613, elbl220617, elbl220623, elbl220628, elbl220708, elbl220712, elbl220717, elbl220719, elbl220720]


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

expID = expID220515 + expID220602 + expID220604 + expID220608 + expID220610 + expID220611 +  expID220613 + expID220617 + expID220623 + expID220628 + expID220708 + expID220712 + expID220717 + expID220719 + expID220720


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

etistr = etistr220515 + etistr220602 + etistr220604 + etistr220608 + etistr220610 + etistr220611 + etistr220613 + etistr220617 + etistr220623 + etistr220628 + etistr220708 + etistr220712 + etistr220717 + etistr220719 + etistr220720

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

etfstr = etfstr220515 + etfstr220602 + etfstr220604 + etfstr220608 + etfstr220610 + etfstr220611 + etfstr220613 + etfstr220617 + etfstr220623 + etfstr220628 + etfstr220708 + etfstr220712 + etfstr220717 + etfstr220719 + etfstr220720

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

cfstr = cf220517 + cf220602 + cf220604 + cf220608 + cf220610 + cf220611 + cf220613 + cf220617 + cf220623 + cf220628 + cf220708 + cf220712 + cf220717 + cf220719 + cf220720

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
Tempi220708 = [0]
Tempi220712 = [0]
Tempi220717 = [0]
Tempi220719 = [0]
Tempi220720 = [0]

Tempi = Tempi220515 + Tempi220602  + Tempi220604  + Tempi220608  + Tempi220610  + Tempi220611  + Tempi220613  + Tempi220617  + Tempi220623  + Tempi220628  + Tempi220708  + Tempi220712  + Tempi220717  + Tempi220719 + Tempi220720

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

AirT = AirT220515 + AirT220602 + AirT220604 + AirT220608 + AirT220610 + AirT220611 + AirT220613 + AirT220617 + AirT220623 + AirT220628 + AirT220708 + AirT220712 + AirT220717 + AirT220719 + AirT220720

# Final temperature filter strings
Tempf220515 = ['17:55:00']
Tempf220602 = [0]
Tempf220604 = [0]
Tempf220608 = [0, 0]
Tempf220610 = [0]
Tempf220611 = [0]
Tempf220613 = [0, 0]
Tempf220617 = [0]
Tempf220623 = ['17:00:00']
Tempf220628 = [0]
Tempf220708 = [0]
Tempf220712 = [0]
Tempf220717 = [0]
Tempf220719 = [0]
Tempf220720 = [0]

Tempf = Tempf220515 + Tempf220602  + Tempf220604  + Tempf220608  + Tempf220610  + Tempf220611  + Tempf220613  + Tempf220617  + Tempf220623  + Tempf220628  + Tempf220708  + Tempf220712  + Tempf220717  + Tempf220719 + Tempf220720

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
ig220628 = ['Ignition without Propegation'] 
ig220708 = ['Ignition']
ig220712 = ['Ignition']
ig220717 = ['Ignition']
ig220719 = ['No']
ig220720 = ['No']

igstr = ig220517 + ig220602 + ig220604 + ig220608 + ig220610 + ig220611 + ig220613 + ig220617 + ig220623 + ig220628 + ig220708 + ig220712 + ig220717 + ig220719 + ig220720

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

conc = conc220517 + conc220602 + conc220604 + conc220608 + conc220610 + conc220611 + conc220613 + conc220617 + conc220623 + conc220628 + conc220708 + conc220712 + conc220717 + conc220719 + conc220720

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

GACbed = GACbed220517 + GACbed220602 + GACbed220604 + GACbed220608 + GACbed220610 + GACbed220611 + GACbed220613 + GACbed220617 + GACbed220623 + GACbed220628 + GACbed220708 + GACbed220712 + GACbed220717 + GACbed220719 + GACbed220720

