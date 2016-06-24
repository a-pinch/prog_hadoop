#! /usr/bin/python3
import sys,re

oldKey = ''
s = 0.0
M = '{}'
for line in sys.stdin:    
    l = line.strip().split() 
    if(not l[0] == oldKey):
        if(oldKey):
            print("%s\t%.3f\t%s" % (oldKey,s,M))
        oldKey = l[0]
        s = 0.0
        M = '{}'
    if(l[2] == '{}'):
        s += float(l[1])
    else:
        M = l[2]
if(oldKey):  print("%s\t%.3f\t%s" % (oldKey,s,M))

