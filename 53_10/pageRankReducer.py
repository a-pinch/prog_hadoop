#! /usr/bin/python3
import sys,re

oldKey = ''
s = 0.0
M = '{}'
k = 0.1*(1.0/5.0)
a = 0.9
for line in sys.stdin:    
    l = line.strip().split() 
    if(not l[0] == oldKey):
        if(oldKey):
            print("%s\t%.3f\t%s" % (oldKey,k+a*s,M))
        oldKey = l[0]
        s = 0.0
        M = '{}'
    if(l[2] == '{}'):
        s += float(l[1])
    else:
        M = l[2]
if(oldKey):  print("%s\t%.3f\t%s" % (oldKey,k+a*s,M))

