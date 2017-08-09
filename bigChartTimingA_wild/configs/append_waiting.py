# python

import json
import sys

filename = sys.argv[1]

with open(filename, 'r') as log:
    json = json.load(log)

print 'Waiting: ' + str(json['Summary'][0][1][1])
