import json
import sys

filename = sys.argv[1]
dbType = sys.argv[2]

with open(filename) as json_data:
    data = json.load(json_data)

rm = 0
r = 0
ws = 0
fws = 0
try:
	rm = data[dbType]['blockByType']['RM']['count']
except KeyError:
        rm = 0
try:
	r = data[dbType]['blockByType']['R']['count']
except KeyError:
        r = 0
try:
	ws = data[dbType]['blockByType']['WS']['count']
except KeyError:
        ws = 0
try:
	fws = data[dbType]['blockByType']['FWS']['count']
except KeyError:
	fws = 0
print 'Runtime: ' + str(data[dbType]['wallTime'] * 1000)
print 'CPU Time: ' + str(data[dbType]['CPUTime'] * 1000)
print 'Total Number of IO Calls: ' + str(data[dbType]['blockIOCount'])
print 'Number of Reads: ' + str(rm + r)
print 'Number of Writes: ' + str(ws)
print 'Number of Flushes: ' + str(fws)
