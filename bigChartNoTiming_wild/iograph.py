import json
import sys

import matplotlib as mpl
mpl.use("pgf")
pgf_with_pdflatex = {
    "pgf.texsystem": "pdflatex",
    "pgf.preamble": [
         r"\usepackage[utf8x]{inputenc}",
         r"\usepackage[T1]{fontenc}",
         r"\usepackage{cmbright}",
         ]
}
mpl.rcParams.update(pgf_with_pdflatex)


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties
from matplotlib import rc,rcParams
from pylab import *
from matplotlib.lines import Line2D

def findColor(s):
	if s == 'R' or s == 'RM':
		return 'Y'
	if s == 'WS':
		return 'B'
	if s == 'FWS':
		return 'R'

used_labels = []
def findLabel(s):
        if s == 'R' or s == 'RM':
		if 'Read' in used_labels:
			return
		used_labels.append('Read')
                return 'Read'
        if s == 'WS':
		if 'Write Sync' in used_labels:
                        return
                used_labels.append('Write Sync')
                return 'Write Sync'
        if s == 'FWS':
		if 'Flush Write Sync' in used_labels:
                        return
                used_labels.append('Flush Write Sync')
                return 'Flush Write Sync'

filename = sys.argv[1]
dbType = sys.argv[2]

with open(filename) as json_data:
    data = json.load(json_data)

ioinfo = data[dbType]['blockIOs']
starttime = data[dbType]['startTime']
runtime = data[dbType]['wallTime'] * 1000

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
ax = plt.figure(1)

numios = 0
for info in ioinfo:
	temp = []
	temp2 = []
	temp.append((info['startTime'] - starttime) * 1000)
	temp.append((info['endTime'] - starttime) * 1000)
	numios += 1
	temp2.append(numios)
	temp2.append(numios)
	plt.plot(temp,temp2,color= findColor(info['operation']),label= findLabel(info['operation']),linewidth=3)

#print starttime
#print numios

'''
plt.rc('text', usetex=True)
plt.rc('font', family='serif')
ax = plt.figure(1)
'''


legend = plt.legend(loc='upper left')
x_range = [0,runtime]
plt.xlim(x_range)
font0 = FontProperties()
font = font0.copy()
#font.set_style('italic')
#font.set_weight('bold')
font.set_size('xx-large')
#font.set_size(22)

plt.ylabel('Number of IO Events (' + str(numios) + ')' ,fontproperties=font)
plt.xlabel('Runtime (ms)',fontproperties=font)
plt.title(sys.argv[1]+' IO (' + sys.argv[2] + ')',fontproperties=font)

#ax.tick_params(axis='x', labelsize=22)
#plt.subplots().set_ylabel(fontsize=22)
#ax.yaxis.label.set_size(40)
ax1 = gca()
ax1.xaxis.set_tick_params(labelsize=16)
ax1.yaxis.set_tick_params(labelsize=16)

fig15 = plt.gcf()
#manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())

# #7FFFD4
name = sys.argv[1]
name = name.split('__')[1]
plt.show()
fig15.savefig('Graphs/IO_' + name)

