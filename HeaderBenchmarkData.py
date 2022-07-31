#!/usr/bin/env python

# Date Strings
BMdatestrs = ['220313', '220314', '220315', '220324', '220331', '220515', '220602', '220604', '220615', '220715']

# File Location and Names for power benchmarks
fpath = '../../Box_Experiments/'

f220313 = '220313_FiberBenchmark/220313_FiberBenchmark_data.csv'
f220314 = '220314_FiberBenchmark/220314_FiberBenchmark_data.csv'
f220315 = '220315_CollectorBenchmark/220315_CollectorBenchmark_data.csv'
f220324 = '220324_CollectorBenchmark/220324_CollectorBenchmark_data.csv'
f220331 = '220331_CollectorFiberBenchmark/220331_CollectorFiberBenchmark_data.csv'
f220515 = '220515_SingleChannel_GACSoil/220515_PowerBenchmark_data.csv'
f220602 = '220602_SingleChannel_GACSoil/220602_PowerBenchmark_data.csv'
f220604 = '220604_SingleChannel_GACSoil/220604_PowerBenchmark_data.csv'
f220615 = '220615_PowerBenchmark/220615_PowerBenchmark_data.csv'
f220715 = '220715_PowerBenchmark/220715_PowerBenchmark_data.csv'

BMfnames = [f220313, f220314, f220315, f220324, f220331, f220515, f220602, f220604, f220615, f220715] # Array of file names

# Labels
lbl220313 = ['C1 FA Before Cleaning', 'C1 FA After Cleaning', 'C1 FB', 'C1 FC', 'C1 FD Backwards', 'C1 FE']
lbl220314 = ['C1 FE Before Cleaning', 'C1 FE After Cleaning', 'C1 FF', 'C1 FG', 'C1 FH', 'C1 FA']
lbl220315 = ['C1 FB', 'C2 FB', 'C3 FB', 'C4 FB', 'C2 FB: Round II']
lbl220324 = ['C2 FB', 'C4 FB', 'C3 FC', 'C1 FC']
lbl220331 = ['C1 FC', 'C2 FA','C3 FF', 'C4 FD']
lbl220515 = ['C1 FC', 'C2 FA', 'C3 FF']
lbl220602 = ['C1 FC', 'C2 FA', 'C3 FF']
lbl220604 = ['C1 FC', 'C3 FF', 'C4 FD']
lbl220615 = ['C1 FC', 'C2 FA', 'C3 FF', 'C4 FD']
lbl220715 = ['C4 FD Before Windex', 'C4 FD After Windex', 'C2 FA Before Windex', 'C2 FA After Windex', 'C1 FC Before Windex', 'C1 FC After Windex']

BMlbl = lbl220313 + lbl220314 + lbl220315 + lbl220324 + lbl220331 + lbl220515 + lbl220602 + lbl220604 + lbl220615 + lbl220715 # Array of labels
lblidx = [lbl220313, lbl220314, lbl220315, lbl220324, lbl220331, lbl220515, lbl220602, lbl220604, lbl220615, lbl220715] # Label array for indexing 

# Initial time strings
tistr220313 = ['12:33:00', '12:40:00', '13:08:00', '13:39:00', '14:21:00', '14:50:00']
tistr220314 = ['11:18:00', '11:29:00', '11:50:00', '13:52:15', '14:25:00', '14:59:00']
tistr220315 = ['12:00:00', '13:01:00', '14:06:00', '15:25:15', '16:25:00']
tistr220324 = ['13:44:00', '14:40:00', '15:32:00', '16:32:00']
tistr220331 = ['13:42:00', '14:16:00', '14:46:00', '15:15:00']
tistr220515 = ['13:03:30', '13:30:00', '13:56:00']
tistr220602 = ['12:36:00', '13:07:00', '13:31:00']
tistr220604 = ['10:45:00', '11:06:00', '11:25:00']
tistr220615 = ['12:41:00', '13:10:00', '13:44:00', '14:15:00']
tistr220715 = ['11:37:00', '12:10:00', '12:41:00', '12:58:00', '13:33:00', '13:47:00']

tistr = tistr220313 + tistr220314 + tistr220315 + tistr220324 + tistr220331 + tistr220515 + tistr220602 + tistr220604 + tistr220615 + tistr220715 # Array of inital time srings

# Final time strings
tfstr220313 = ['12:38:00', '12:45:00', '13:18:00', '13:52:00', '14:30:00', '14:58:00']
tfstr220314 = ['11:28:00', '11:35:15', '11:58:00', '14:04:00', '14:36:00', '15:10:00']
tfstr220315 = ['12:10:00', '13:11:00', '14:17:00', '15:36:00', '16:35:00']
tfstr220324 = ['13:54:00', '14:50:00', '15:42:00', '16:44:00']
tfstr220331 = ['13:52:00', '14:26:00', '14:56:00', '15:26:00']
tfstr220515 = ['13:14:00', '13:41:00', '15:52:00']
tfstr220602 = ['12:47:00', '13:14:00', '13:40:00']
tfstr220604 = ['10:52:00', '11:12:00', '11:31:00']
tfstr220615 = ['12:53:00', '13:20:00', '13:56:00', '14:27:00']
tfstr220715 = ['11:58:00', '12:20:00', '12:51:00', '13:09:00', '13:39:00', '14:08:00']

tfstr = tfstr220313 + tfstr220314 + tfstr220315 + tfstr220324 + tfstr220331 + tfstr220515 + tfstr220602 + tfstr220604 + tfstr220615 + tfstr220715 # Array of final time srings
