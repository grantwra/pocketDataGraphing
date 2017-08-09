#usage : python barGraphByDB.py (SQL || BDB || H2) (Workload)

import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

path_to_default = 'configs/defaultSQLBDB/info/' #sql and bdb
path_to_bdb100_cache = 'configs/BDB100MBCache/info/' #bdb
#path_to_heap25 = 'configs/heap25SQLBDB/info/' #sql and bdb
path_to_heap50 = 'configs/heap50SQLBDB/info/' #sql and bdb
path_to_heap25 = 'configs/heap25SQLBDB/info/' #sql and bdb
path_to_h2_after_every = 'configs/H2AfterEveryOp/info/' #h2
path_to_h2_after_burst = 'configs/H2AfterEveryBurst/info/' #h2
path_to_h2_after_end = 'configs/H2AfterEnd/info/' #h2
path_to_kv = 'configs/KV/info/' #kv

default_sql = path_to_default + sys.argv[2] + '_SQL'
default_bdb = path_to_default + sys.argv[2] + '_BDB'
bdb100 = path_to_bdb100_cache + sys.argv[2] + '_BDB'
#heap25_sql = path_to_heap25 + sys.argv[2] + '_SQL'
#heap25_bdb = path_to_heap25 + sys.argv[2] + '_BDB'
heap50_sql = path_to_heap50 + sys.argv[2] + '_SQL'
heap50_bdb = path_to_heap50 + sys.argv[2] + '_BDB'
heap25_sql = path_to_heap25 + sys.argv[2] + '_SQL'
heap25_bdb = path_to_heap25 + sys.argv[2] + '_BDB'
h2_every = path_to_h2_after_every + sys.argv[2] + '_H2'
h2_burst = path_to_h2_after_burst + sys.argv[2] + '_H2'
h2_end = path_to_h2_after_end  + sys.argv[2] + '_H2'
kv = path_to_kv  + sys.argv[2] + '_KV'
kv_load = path_to_kv  + sys.argv[2] + '_LOAD'
kv_save = path_to_kv  + sys.argv[2] + '_SAVE'
kv_quer = path_to_kv  + sys.argv[2] + '_QUERIES'

'''
default_sqla = path_to_default +'A_SQL'
default_sqlb = path_to_kv  + sys.argv[2] + '_KV'
default_sqlc = path_to_default +'C_SQL'
default_sqld = path_to_default +'D_SQL'
default_sqle = path_to_default +'E_SQL'
default_sqlf = path_to_default +'F_SQL'
default_sqlia = path_to_default +'IA_SQL'
default_sqlib = path_to_default +'IB_SQL'
default_sqlic = path_to_default +'IC_SQL'
'''

sqlfileList = []
bdbfileList = []
h2fileList = []
kvfileList = []

sqlfileList.append(default_sql)
bdbfileList.append(default_bdb)
bdbfileList.append(bdb100)
sqlfileList.append(heap50_sql)
bdbfileList.append(heap50_bdb)
sqlfileList.append(heap25_sql)
bdbfileList.append(heap25_bdb)
h2fileList.append(h2_every)
h2fileList.append(h2_burst)
h2fileList.append(h2_end)
kvfileList.append(kv_load)
kvfileList.append(kv_quer)
kvfileList.append(kv_save)
kvfileList.append(kv)

cpu_list = []
run_list = []
read_list = []
write_list = []
flush_list = []

if sys.argv[1] == 'SQL':

	for name in sqlfileList:
		with open(name,'r') as log:
			for line in log:
				if 'CPU' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        cpu_list.append(float(numFinal))

				if 'Runtime' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        run_list.append(float(numFinal))


				if 'Reads' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        read_list.append(float(numFinal))

                                if 'Writes' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        write_list.append(float(numFinal))

                                if 'Flushes' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        flush_list.append(float(numFinal))
	##
	#N = 6
	#ind = np.arange(N)
	#fig, ax = plt.subplots(221)
	#width = .25
	#barlist = ax
	fig = plt.figure()
	fig.canvas.set_window_title('SQL Workload ' + sys.argv[2]) 
	fig.subplots_adjust(left=0.2, wspace=0.6)
	ax1 = fig.add_subplot(211)
	N = 3
	ind = np.arange(N)
	width = .4
	ax1.bar(ind,cpu_list,width,color='b',alpha = .5,label='CPU Time')
        ax1.bar(ind + width, run_list,width,color='r',alpha=.5,label='Runtime')
	ax1.legend(loc='upper left')	

	manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())

	width = .3

	ax2 = fig.add_subplot(212)
	ax2.bar(ind,flush_list,width,color='b',alpha = .75,label='Flush')
        #ax2.bar(ind + width + width, write_list,width,color='g',label='Write')
	ax2.bar(ind + width, read_list,width,color='y',alpha = .75,label='Read')
	ax2.bar(ind + width + width, write_list,width,color='g',alpha = .75,label='Write')

	ax2.legend(loc='upper left')

	#fig.suptitle(sys.argv[1] + ' Workload ' + sys.argv[2], fontsize=24)

	#plt.subplots_adjust(top=0.85)

	plt.tight_layout()
	#fig.set_title(sys.argv[1] + ' Workload ' + sys.argv[2])
	ax1.set_title('CPU Time VS Runtime')
	ax2.set_title('Reads VS Writes VS Flushes')
	ax1.set_xticks(ind + .4)
	from textwrap import wrap

	labels = ['Default SQL','SQL with Heap Restricted to 50%', 'SQL with Heap Restricted to 25%']	
	labels = [ '\n'.join(wrap(l, 15)) for l in labels ]
        ax1.set_xticklabels(labels)
	ax2.set_xticks(ind + .46)
	ax2.set_xticklabels(labels)
	ax1.set_ylabel('Time in milliseconds')
	ax2.set_ylabel('Number of IO Events')

	fig15 = plt.gcf()
	plt.show()

	fig15.savefig('Graphs/byDb/' + sys.argv[1] + '_' + sys.argv[2])



if sys.argv[1] == 'BDB':

        for name in bdbfileList:
                with open(name,'r') as log:
                        for line in log:
                                if 'CPU' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        cpu_list.append(float(numFinal))

                                if 'Runtime' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        run_list.append(float(numFinal))


                                if 'Reads' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        read_list.append(float(numFinal))

                                if 'Writes' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        write_list.append(float(numFinal))

                                if 'Flushes' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        flush_list.append(float(numFinal))
        ##
        #N = 6
        #ind = np.arange(N)
        #fig, ax = plt.subplots(221)
        #width = .25
        #barlist = ax
	fig = plt.figure()
        fig.canvas.set_window_title('BDB Workload ' + sys.argv[2])
        fig.subplots_adjust(left=0.2, wspace=0.6)
        ax1 = fig.add_subplot(211)
        N = 4
        ind = np.arange(N)
        width = .4
        ax1.bar(ind,cpu_list,width,color='b',alpha = .5,label='CPU Time')
        ax1.bar(ind + width, run_list,width,color='r',alpha=.5,label='Runtime')
        ax1.legend(loc='upper left')

        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())

        width = .3

        ax2 = fig.add_subplot(212)
        ax2.bar(ind,flush_list,width,color='b',alpha = .75,label='Flush')
        #ax2.bar(ind + width + width, write_list,width,color='g',label='Write')
        ax2.bar(ind + width, read_list,width,color='y',alpha = .75,label='Read')
        ax2.bar(ind + width + width, write_list,width,color='g',alpha = .75,label='Write')

        ax2.legend(loc='upper left')

        #fig.suptitle(sys.argv[1] + ' Workload ' + sys.argv[2], fontsize=24)

        #plt.subplots_adjust(top=0.85)

        plt.tight_layout()
        #fig.set_title(sys.argv[1] + ' Workload ' + sys.argv[2])
        ax1.set_title('CPU Time VS Runtime')
        ax2.set_title('Reads VS Writes VS Flushes')
        ax1.set_xticks(ind + .4)
        from textwrap import wrap

        labels = ['Default BDB','BDB with 100MB Cache','BDB with Heap Restricted to 50%', 'BDB with Heap Restricted to 25%']
        labels = [ '\n'.join(wrap(l, 15)) for l in labels ]
        ax1.set_xticklabels(labels)
        ax2.set_xticks(ind + .46)
        ax2.set_xticklabels(labels)
        ax1.set_ylabel('Time in milliseconds')
        ax2.set_ylabel('Number of IO Events')

        fig15 = plt.gcf()
        plt.show()

        fig15.savefig('Graphs/byDb/' + sys.argv[1] + '_' + sys.argv[2])


if sys.argv[1] == 'H2':

        for name in h2fileList:
                with open(name,'r') as log:
                        for line in log:
                                if 'CPU' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        cpu_list.append(float(numFinal))

                                if 'Runtime' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        run_list.append(float(numFinal))


                                if 'Reads' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        read_list.append(float(numFinal))

                                if 'Writes' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        write_list.append(float(numFinal))

                                if 'Flushes' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        flush_list.append(float(numFinal))
        ##
        #N = 6
        #ind = np.arange(N)
        #fig, ax = plt.subplots(221)
        #width = .25
        #barlist = ax
	fig = plt.figure()
        fig.canvas.set_window_title('H2 Workload ' + sys.argv[2])
        fig.subplots_adjust(left=0.2, wspace=0.6)
        ax1 = fig.add_subplot(211)
        N = 3
        ind = np.arange(N)
        width = .4
        ax1.bar(ind,cpu_list,width,color='b',alpha = .5,label='CPU Time')
        ax1.bar(ind + width, run_list,width,color='r',alpha=.5,label='Runtime')
        ax1.legend(loc='upper left')

        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())

        width = .3

        ax2 = fig.add_subplot(212)
        ax2.bar(ind,flush_list,width,color='b',alpha = .75,label='Flush')
        #ax2.bar(ind + width + width, write_list,width,color='g',label='Write')
        ax2.bar(ind + width, read_list,width,color='y',alpha = .75,label='Read')
        ax2.bar(ind + width + width, write_list,width,color='g',alpha = .75,label='Write')

        ax2.legend(loc='upper left')

        #fig.suptitle(sys.argv[1] + ' Workload ' + sys.argv[2], fontsize=24)

        #plt.subplots_adjust(top=0.85)

        plt.tight_layout()
        #fig.set_title(sys.argv[1] + ' Workload ' + sys.argv[2])
        ax1.set_title('CPU Time VS Runtime')
        ax2.set_title('Reads VS Writes VS Flushes')
        ax1.set_xticks(ind + .4)
        from textwrap import wrap

        labels = ['H2 with Sync After Every Query','H2 with Sync after Every Burst (50 Queries)', 'H2 with Sync at End']
        labels = [ '\n'.join(wrap(l, 25)) for l in labels ]
        ax1.set_xticklabels(labels)
        ax2.set_xticks(ind + .46)
        ax2.set_xticklabels(labels)
        ax1.set_ylabel('Time in milliseconds')
        ax2.set_ylabel('Number of IO Events')

        fig15 = plt.gcf()
        plt.show()

        fig15.savefig('Graphs/byDb/' + sys.argv[1] + '_' + sys.argv[2])

if sys.argv[1] == 'KV':

        for name in kvfileList:
                with open(name,'r') as log:
                        for line in log:
                                if 'CPU' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        cpu_list.append(float(numFinal))

                                if 'Runtime' in line:
                                        column = line.split(':')
                                        num = column[1].replace(' ','')
                                        numFinal = num.replace('\n','')
                                        #print numFinal
                                        run_list.append(float(numFinal))

	fig = plt.figure()
        fig.canvas.set_window_title('KV Workload ' + sys.argv[2])
        fig.subplots_adjust(left=0.2, wspace=0.6)
        ax1 = fig.add_subplot(111)
        N = 4
        ind = np.arange(N)
        width = .4
        ax1.bar(ind,cpu_list,width,color='b',alpha = .5,label='CPU Time')
        ax1.bar(ind + width, run_list,width,color='r',alpha=.5,label='Runtime')
        ax1.legend(loc='upper left')

        manager = plt.get_current_fig_manager()
        manager.resize(*manager.window.maxsize())

        width = .3

        #ax2 = fig.add_subplot(212)
        #ax2.bar(ind,flush_list,width,color='b',alpha = .75,label='Flush')
        #ax2.bar(ind + width + width, write_list,width,color='g',label='Write')
        #ax2.bar(ind + width, read_list,width,color='y',alpha = .75,label='Read')
        #ax2.bar(ind + width + width, write_list,width,color='g',alpha = .75,label='Write')

	#ax2.legend(loc='upper left')

        #fig.suptitle(sys.argv[1] + ' Workload ' + sys.argv[2], fontsize=24)

        #plt.subplots_adjust(top=0.85)

        plt.tight_layout()
        #fig.set_title(sys.argv[1] + ' Workload ' + sys.argv[2])
        ax1.set_title('CPU Time VS Runtime')
        #ax2.set_title('Reads VS Writes VS Flushes')
        ax1.set_xticks(ind + .4)
        from textwrap import wrap

        labels = ['KV Load','KV Queries','KV Save','KV Total']
        labels = [ '\n'.join(wrap(l, 25)) for l in labels ]
        ax1.set_xticklabels(labels)
        #ax2.set_xticks(ind + .46)
        #ax2.set_xticklabels(labels)
        ax1.set_ylabel('Time in milliseconds')
        #ax2.set_ylabel('Number of IO Events')

        fig15 = plt.gcf()

	plt.show()

        fig15.savefig('Graphs/byDb/' + sys.argv[1] + '_' + sys.argv[2])

