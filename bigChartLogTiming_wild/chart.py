#usage:
#Need to build information by using barGraph.py
#then simply call 'python chart.py'

import matplotlib.pyplot as plt
import scipy
import numpy as np


path_cpu_a = 'Graphs/info/CPU_A'
path_cpu_b = 'Graphs/info/CPU_B'
path_cpu_c = 'Graphs/info/CPU_C'
path_cpu_d = 'Graphs/info/CPU_D'
path_cpu_e = 'Graphs/info/CPU_E'
path_cpu_f = 'Graphs/info/CPU_F'
path_cpu_ia = 'Graphs/info/CPU_IA'
path_cpu_ib = 'Graphs/info/CPU_IB'
path_cpu_ic = 'Graphs/info/CPU_IC'

path_run_a = 'Graphs/info/RUN_A'
path_run_b = 'Graphs/info/RUN_B'
path_run_c = 'Graphs/info/RUN_C'
path_run_d = 'Graphs/info/RUN_D'
path_run_e = 'Graphs/info/RUN_E'
path_run_f = 'Graphs/info/RUN_F'
path_run_ia = 'Graphs/info/RUN_IA'
path_run_ib = 'Graphs/info/RUN_IB'
path_run_ic = 'Graphs/info/RUN_IC'

path_io_a = 'Graphs/info/IO_A'
path_io_b = 'Graphs/info/IO_B'
path_io_c = 'Graphs/info/IO_C'
path_io_d = 'Graphs/info/IO_D'
path_io_e = 'Graphs/info/IO_E'
path_io_f = 'Graphs/info/IO_F'
path_io_ia = 'Graphs/info/IO_IA'
path_io_ib = 'Graphs/info/IO_IB'
path_io_ic = 'Graphs/info/IO_IC'

def returninfo(path,flag):
	if flag == 0:
		with open(path,'r') as log:
			#values = []
			for line in log:
				columns = line.split(' ')
				tier2 = columns[1].split(':')
				return tier2[0]

	if flag == 1:
		with open(path,'r') as log:
			values = []
			for line in log:
				columns = line.split(':')
				values.append(float(columns[1]))
			diff = values[1] - values [0]
			percent = diff / values[0]
			finpercent = round(percent * 100,2)
			return str(finpercent)


def totalioinfo(path,flag):
	if flag == 0:
                with open(path,'r') as log:
                        #values = []
                        for line in log:
				if 'Total' in line:
                                	columns = line.split('. ')
                                	tier2 = columns[1].split(':')
                                	return tier2[0]

        if flag == 1:
                with open(path,'r') as log:
                        values = []
                        for line in log:
				if 'Total' in line:
                                	columns = line.split(':')
                                	values.append(float(columns[1]))
                        diff = values[1] - values [0]
                        percent = diff / values[0]
                        finpercent = round(percent * 100,2)
                        return str(finpercent)

def readioinfo(path,flag):
        if flag == 0:
                with open(path,'r') as log:
                        #values = []
                        for line in log:
                                if 'Reads' in line:
                                        columns = line.split('. ')
                                        tier2 = columns[1].split(':')
                                	return tier2[0]

        if flag == 1:
                with open(path,'r') as log:
                        values = []
                        for line in log:
                                if 'Reads' in line:
                                        columns = line.split(':')
                                        values.append(float(columns[1]))
                        diff = values[1] - values [0]
                        percent = diff / values[0]
                        finpercent = round(percent * 100,2)
                        return str(finpercent)

def writeioinfo(path,flag):
        if flag == 0:
                with open(path,'r') as log:
                        #values = []
                        for line in log:
                                if 'Writes' in line:
                                        columns = line.split('. ')
                                        tier2 = columns[1].split(':')
                                	return tier2[0]

        if flag == 1:
                with open(path,'r') as log:
                        values = []
                        for line in log:
                                if 'Writes' in line:
                                        columns = line.split(':')
                                        values.append(float(columns[1]))
                        diff = values[1] - values [0]
			if values[0] == 0:
				return str(diff * 100)
                        percent = diff / values[0]
                        finpercent = round(percent * 100,2)
                        return str(finpercent)


def flushioinfo(path,flag):
        if flag == 0:
                with open(path,'r') as log:
                        #values = []
                        for line in log:
                                if 'Flushes' in line:
                                        columns = line.split('. ')
                                        tier2 = columns[1].split(':')
                                	return tier2[0]

        if flag == 1:
                with open(path,'r') as log:
                        values = []
                        for line in log:
                                if 'Flushes' in line:
                                        columns = line.split(':')
                                        values.append(float(columns[1]))
                        diff = values[1] - values [0]
                        percent = diff / values[0]
                        finpercent = round(percent * 100,2)
                        return str(finpercent)


#N = 10
#ind = np.arange(0,N,1)

#fig, ax = plt.subplots()
#plt.xlim(0,10)
#plt.ylim(0,6)
#plt.rc('grid', linestyle='-', color='b')
#plt.grid(b=True, which='both', color='black',linestyle='-')
#plt.grid(True)
#manager = plt.get_current_fig_manager()
#manager.resize(*manager.window.maxsize())
#ax.set_xticks(scipy.arange(0,10,1))
#for axis in [ax.xaxis, ax.yaxis]:
 #   axis.set(ticks=np.arange(0.5, len(labels)), ticklabels=labels)
#ax.set_xticks(ind + 0.5)
#ax.set_xticklabels(False)
from textwrap import wrap
labels = [ 'Workload A', 'Workload B', 'Workload C', 'Workload D', 'Workload E', 'Workload F','Workload IA' , 'Workload IB', 'Workload IC' ]
labels = [ '\n'.join(wrap(l, 12)) for l in labels ]

labels2 = [ 'Number of Flushes', 'Number of Writes', 'Number of Reads', 'Total IO', 'CPU Time', 'Runtime', 'Difference in Runtime between first and second best' ]
labels2 = [ '\n'.join(wrap(l, 12)) for l in labels2 ]

#ax.set_xticklabels(labels)
#for axis in [ax.xaxis, ax.yaxis]:
#    axis.set(ticks=np.arange(0.5, len(labels)), ticklabels=labels)

#plt.show()

#data = np.random.random((6,9))
percentdiffa = 0.0
percentdiffb = 0.0
percentdiffc = 0.0
percentdiffd = 0.0
percentdiffe = 0.0
percentdifff = 0.0
percentdiffia = 0.0
percentdiffib = 0.0
percentdiffic = 0.0

with open(path_run_a,'r') as log:
	temp = []
	for line in log:
		columns = line.split(':')
		temp.append(float(columns[1]))
	diff = temp[1] - temp[0]
	percent = diff / temp[0]
	percent2 = percent * 2
	per1 = percent2 - 1
	per2 = per1 / -1
	percentdiffa = per2

with open(path_run_b,'r') as log:
        temp = []
        for line in log:
                columns = line.split(':')
                temp.append(float(columns[1]))
        diff = temp[1] - temp[0]
        percent = diff / temp[0]
        percent2 = percent * 2
        per1 = percent2 - 1
        per2 = per1 / -1
        percentdiffb = per2

with open(path_run_c,'r') as log:
        temp = []
        for line in log:
                columns = line.split(':')
                temp.append(float(columns[1]))
        diff = temp[1] - temp[0]
        percent = diff / temp[0]
        percent2 = percent * 2
        per1 = percent2 - 1
        per2 = per1 / -1
        percentdiffc = per2

with open(path_run_d,'r') as log:
        temp = []
        for line in log:
                columns = line.split(':')
                temp.append(float(columns[1]))
        diff = temp[1] - temp[0]
        percent = diff / temp[0]
        percent2 = percent * 2
        per1 = percent2 - 1
        per2 = per1 / -1
        percentdiffd = per2

with open(path_run_e,'r') as log:
        temp = []
        for line in log:
                columns = line.split(':')
                temp.append(float(columns[1]))
        diff = temp[1] - temp[0]
        percent = diff / temp[0]
        percent2 = percent * 2
        per1 = percent2 - 1
        per2 = per1 / -1
        percentdiffe = per2

with open(path_run_f,'r') as log:
        temp = []
        for line in log:
                columns = line.split(':')
                temp.append(float(columns[1]))
        diff = temp[1] - temp[0]
        percent = diff / temp[0]
        percent2 = percent * 2
        per1 = percent2 - 1
        per2 = per1 / -1
        percentdifff = per2

with open(path_run_ia,'r') as log:
        temp = []
        for line in log:
                columns = line.split(':')
                temp.append(float(columns[1]))
        diff = temp[1] - temp[0]
        percent = diff / temp[0]
        percent2 = percent * 2
        per1 = percent2 - 1
        per2 = per1 / -1
        percentdiffia = per2

with open(path_run_ib,'r') as log:
        temp = []
        for line in log:
                columns = line.split(':')
                temp.append(float(columns[1]))
        diff = temp[1] - temp[0]
        percent = diff / temp[0]
        percent2 = percent * 2
        per1 = percent2 - 1
        per2 = per1 / -1
        percentdiffib = per2

with open(path_run_ic,'r') as log:
        temp = []
        for line in log:
                columns = line.split(':')
                temp.append(float(columns[1]))
        diff = temp[1] - temp[0]
        percent = diff / temp[0]
        percent2 = percent * 2
        per1 = percent2 - 1
        per2 = per1 / -1
        percentdiffic = per2

#print percentdiffib

#                 	Flushes			Writes			Reads	     Total IO		CPU			Runtime
data = np.array([[1, 1, 1, 1,1,1,1,1,1],[1, 1, 1, 1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1],[percentdiffa,percentdiffb,percentdiffc,percentdiffd,percentdiffe,percentdifff,percentdiffia,percentdiffib,percentdiffic]])
#data = 0
#labels = 'abcdefghij'

fig, ax = plt.subplots()
im = ax.pcolor(data, cmap='gray', edgecolor='black', linestyle='-', lw=1,vmin = 0,vmax=1)
cbar = fig.colorbar(im,ticks=[0, 0.5, 1])
cbar.ax.set_yticklabels(['Drastically Different (50% or more longer)', '(Scale for top row only)', 'No Difference (0%)'])

# Shift ticks to be at 0.5, 1.5, etc
for axis in [ax.xaxis]:
    axis.set(ticks=np.arange(0.5, len(labels)), ticklabels=labels)

for axis in [ax.yaxis]:
    axis.set(ticks=np.arange(0.5, len(labels2)), ticklabels=labels2)

manager = plt.get_current_fig_manager()
manager.resize(*manager.window.maxsize())

#test = 'test'
a_flush = (.1,.3)
b_flush = (1.1,.3)
c_flush = (2.1,.3)
d_flush = (3.1,.3)
e_flush = (4.1,.3)
f_flush = (5.1,.3)
ia_flush = (6.1,.3)
ib_flush = (7.1,.3)
ic_flush = (8.1,.3)

a_write = (.1,1.3)
b_write = (1.1,1.3)
c_write = (2.1,1.3)
d_write = (3.1,1.3)
e_write = (4.1,1.3)
f_write = (5.1,1.3)
ia_write = (6.1,1.3)
ib_write = (7.1,1.3)
ic_write = (8.1,1.3)

a_read = (.1,2.3)
b_read = (1.1,2.3)
c_read = (2.1,2.3)
d_read = (3.1,2.3)
e_read = (4.1,2.3)
f_read = (5.1,2.3)
ia_read = (6.1,2.3)
ib_read = (7.1,2.3)
ic_read = (8.1,2.3)

a_io = (.1,3.3)
b_io = (1.1,3.3)
c_io = (2.1,3.3)
d_io = (3.1,3.3)
e_io = (4.1,3.3)
f_io = (5.1,3.3)
ia_io = (6.1,3.3)
ib_io = (7.1,3.3)
ic_io = (8.1,3.3)

a_cpu = (.1,4.3)
b_cpu = (1.1,4.3)
c_cpu = (2.1,4.3)
d_cpu = (3.1,4.3)
e_cpu = (4.1,4.3)
f_cpu = (5.1,4.3)
ia_cpu = (6.1,4.3)
ib_cpu = (7.1,4.3)
ic_cpu = (8.1,4.3)

a_run = (.1,5.3)
b_run = (1.1,5.3)
c_run = (2.1,5.3)
d_run = (3.1,5.3)
e_run = (4.1,5.3)
f_run = (5.1,5.3)
ia_run = (6.1,5.3)
ib_run = (7.1,5.3)
ic_run = (8.1,5.3)

####################################################################################################

#tester = returninfo(path_run_a, 0)
#print tester
#tester2 = returninfo(path_run_a,1)
#print tester2readioinfo(path_io_a,0) + '\n' + readioinfo(path_io_a,1) + '%'

a_flush_info = flushioinfo(path_io_a,0) + '\n' + flushioinfo(path_io_a,1) + '%'
b_flush_info = flushioinfo(path_io_b,0) + '\n' + flushioinfo(path_io_b,1) + '%'
c_flush_info = flushioinfo(path_io_c,0) + '\n' + flushioinfo(path_io_c,1) + '%'
d_flush_info = flushioinfo(path_io_d,0) + '\n' + flushioinfo(path_io_d,1) + '%'
e_flush_info = flushioinfo(path_io_e,0) + '\n' + flushioinfo(path_io_e,1) + '%'
f_flush_info = flushioinfo(path_io_f,0) + '\n' + flushioinfo(path_io_f,1) + '%'
ia_flush_info = flushioinfo(path_io_ia,0) + '\n' + flushioinfo(path_io_ia,1) + '%'
ib_flush_info = flushioinfo(path_io_ib,0) + '\n' + flushioinfo(path_io_ib,1) + '%'
ic_flush_info = flushioinfo(path_io_ic,0) + '\n' + flushioinfo(path_io_ic,1) + '%'

a_write_info = writeioinfo(path_io_a,0) + '\n' + writeioinfo(path_io_a,1) + '%'
b_write_info = writeioinfo(path_io_b,0) + '\n' + writeioinfo(path_io_b,1) + '%'
c_write_info = writeioinfo(path_io_c,0) + '\n' + writeioinfo(path_io_c,1) + '%'
d_write_info = writeioinfo(path_io_d,0) + '\n' + writeioinfo(path_io_d,1) + '%'
e_write_info = writeioinfo(path_io_e,0) + '\n' + writeioinfo(path_io_e,1) + '%'
f_write_info = writeioinfo(path_io_f,0) + '\n' + writeioinfo(path_io_f,1) + '%'
ia_write_info = writeioinfo(path_io_ia,0) + '\n' + writeioinfo(path_io_ia,1) + '%'
ib_write_info = writeioinfo(path_io_ib,0) + '\n' + writeioinfo(path_io_ib,1) + '%'
ic_write_info = writeioinfo(path_io_ic,0) + '\n' + writeioinfo(path_io_ic,1) + '%'

a_read_info = readioinfo(path_io_a,0) + '\n' + readioinfo(path_io_a,1) + '%'
b_read_info = readioinfo(path_io_b,0) + '\n' + readioinfo(path_io_b,1) + '%'
c_read_info = readioinfo(path_io_c,0) + '\n' + readioinfo(path_io_c,1) + '%'
d_read_info = readioinfo(path_io_d,0) + '\n' + readioinfo(path_io_d,1) + '%'
e_read_info = readioinfo(path_io_e,0) + '\n' + readioinfo(path_io_e,1) + '%'
f_read_info = readioinfo(path_io_f,0) + '\n' + readioinfo(path_io_f,1) + '%'
ia_read_info = readioinfo(path_io_ia,0) + '\n' + readioinfo(path_io_ia,1) + '%'
ib_read_info = readioinfo(path_io_ib,0) + '\n' + readioinfo(path_io_ib,1) + '%'
ic_read_info = readioinfo(path_io_ic,0) + '\n' + readioinfo(path_io_ic,1) + '%'

a_io_info = totalioinfo(path_io_a,0) + '\n' + totalioinfo(path_io_a,1) + '%'
b_io_info = totalioinfo(path_io_b,0) + '\n' + totalioinfo(path_io_b,1) + '%'
c_io_info = totalioinfo(path_io_c,0) + '\n' + totalioinfo(path_io_c,1) + '%'
d_io_info = totalioinfo(path_io_d,0) + '\n' + totalioinfo(path_io_d,1) + '%'
e_io_info = totalioinfo(path_io_e,0) + '\n' + totalioinfo(path_io_e,1) + '%'
f_io_info = totalioinfo(path_io_f,0) + '\n' + totalioinfo(path_io_f,1) + '%'
ia_io_info = totalioinfo(path_io_ia,0) + '\n' + totalioinfo(path_io_ia,1) + '%'
ib_io_info = totalioinfo(path_io_ib,0) + '\n' + totalioinfo(path_io_ib,1) + '%'
ic_io_info = totalioinfo(path_io_ic,0) + '\n' + totalioinfo(path_io_ic,1) + '%'

a_cpu_info = returninfo(path_cpu_a,0) + '\n' + returninfo(path_cpu_a,1) + '%'   #'a cpu'
b_cpu_info = returninfo(path_cpu_b,0) + '\n' + returninfo(path_cpu_b,1) + '%' #'b cpu'
c_cpu_info = returninfo(path_cpu_c,0) + '\n' + returninfo(path_cpu_c,1) + '%'
d_cpu_info = returninfo(path_cpu_d,0) + '\n' + returninfo(path_cpu_d,1) + '%'
e_cpu_info = returninfo(path_cpu_e,0) + '\n' + returninfo(path_cpu_e,1) + '%'
f_cpu_info = returninfo(path_cpu_f,0) + '\n' + returninfo(path_cpu_f,1) + '%'
ia_cpu_info = returninfo(path_cpu_ia,0) + '\n' + returninfo(path_cpu_ia,1) + '%'
ib_cpu_info = returninfo(path_cpu_ib,0) + '\n' + returninfo(path_cpu_ib,1) + '%'
ic_cpu_info = returninfo(path_cpu_ic,0) + '\n' + returninfo(path_cpu_ic,1) + '%'

a_run_info = returninfo(path_run_a,0) + '\n' + returninfo(path_run_a,1) + '%'
b_run_info = returninfo(path_run_b,0) + '\n' + returninfo(path_run_b,1) + '%'
c_run_info = returninfo(path_run_c,0) + '\n' + returninfo(path_run_c,1) + '%'
d_run_info = returninfo(path_run_d,0) + '\n' + returninfo(path_run_d,1) + '%'
e_run_info = returninfo(path_run_e,0) + '\n' + returninfo(path_run_e,1) + '%'
f_run_info = returninfo(path_run_f,0) + '\n' + returninfo(path_run_f,1) + '%'
ia_run_info = returninfo(path_run_ia,0) + '\n' + returninfo(path_run_ia,1) + '%'
ib_run_info = returninfo(path_run_ib,0) + '\n' + returninfo(path_run_ib,1) + '%'
ic_run_info = returninfo(path_run_ic,0) + '\n' + returninfo(path_run_ic,1) + '%'

ax.annotate(a_flush_info, xy=a_flush,fontsize=15)
ax.annotate(b_flush_info, xy=b_flush,fontsize=15)
ax.annotate(c_flush_info, xy=c_flush,fontsize=15)
ax.annotate(d_flush_info, xy=d_flush,fontsize=15)
ax.annotate(e_flush_info, xy=e_flush,fontsize=15)
ax.annotate(f_flush_info, xy=f_flush,fontsize=15)
ax.annotate(ia_flush_info, xy=ia_flush,fontsize=15)
ax.annotate(ib_flush_info, xy=ib_flush,fontsize=15)
ax.annotate(ic_flush_info, xy=ic_flush,fontsize=15)

ax.annotate(a_write_info, xy=a_write,fontsize=15)
ax.annotate(b_write_info, xy=b_write,fontsize=15)
ax.annotate(c_write_info, xy=c_write,fontsize=15)
ax.annotate(d_write_info, xy=d_write,fontsize=15)
ax.annotate(e_write_info, xy=e_write,fontsize=15)
ax.annotate(f_write_info, xy=f_write,fontsize=15)
ax.annotate(ia_write_info, xy=ia_write,fontsize=15)
ax.annotate(ib_write_info, xy=ib_write,fontsize=15)
ax.annotate(ic_write_info, xy=ic_write,fontsize=15)

ax.annotate(a_read_info, xy=a_read,fontsize=15)
ax.annotate(b_read_info, xy=b_read,fontsize=15)
ax.annotate(c_read_info, xy=c_read,fontsize=15)
ax.annotate(d_read_info, xy=d_read,fontsize=15)
ax.annotate(e_read_info, xy=e_read,fontsize=15)
ax.annotate(f_read_info, xy=f_read,fontsize=15)
ax.annotate(ia_read_info, xy=ia_read,fontsize=15)
ax.annotate(ib_read_info, xy=ib_read,fontsize=15)
ax.annotate(ic_read_info, xy=ic_read,fontsize=15)

ax.annotate(a_io_info, xy=a_io,fontsize=15)
ax.annotate(b_io_info, xy=b_io,fontsize=15)
ax.annotate(c_io_info, xy=c_io,fontsize=15)
ax.annotate(d_io_info, xy=d_io,fontsize=15)
ax.annotate(e_io_info, xy=e_io,fontsize=15)
ax.annotate(f_io_info, xy=f_io,fontsize=15)
ax.annotate(ia_io_info, xy=ia_io,fontsize=15)
ax.annotate(ib_io_info, xy=ib_io,fontsize=15)
ax.annotate(ic_io_info, xy=ic_io,fontsize=15)

ax.annotate(a_cpu_info, xy=a_cpu,fontsize=15)
ax.annotate(b_cpu_info, xy=b_cpu,fontsize=15)
ax.annotate(c_cpu_info, xy=c_cpu,fontsize=15)
ax.annotate(d_cpu_info, xy=d_cpu,fontsize=15)
ax.annotate(e_cpu_info, xy=e_cpu,fontsize=15)
ax.annotate(f_cpu_info, xy=f_cpu,fontsize=15)
ax.annotate(ia_cpu_info, xy=ia_cpu,fontsize=15)
ax.annotate(ib_cpu_info, xy=ib_cpu,fontsize=15)
ax.annotate(ic_cpu_info, xy=ic_cpu,fontsize=15)

ax.annotate(a_run_info, xy=a_run,fontsize=15)
ax.annotate(b_run_info, xy=b_run,fontsize=15)
ax.annotate(c_run_info, xy=c_run,fontsize=15)
ax.annotate(d_run_info, xy=d_run,fontsize=15)
ax.annotate(e_run_info, xy=e_run,fontsize=15)
ax.annotate(f_run_info, xy=f_run,fontsize=15)
ax.annotate(ia_run_info, xy=ia_run,fontsize=15)
ax.annotate(ib_run_info, xy=ib_run,fontsize=15)
ax.annotate(ic_run_info, xy=ic_run,fontsize=15)


fig15 = plt.gcf()
plt.show()
fig15.savefig('bigChart.png')
