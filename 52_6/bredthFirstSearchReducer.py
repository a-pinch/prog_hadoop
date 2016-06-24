#! /usr/bin/python3
import sys,re

oldKey = ''
dMin = -1
M = '{}'
for line in sys.stdin:    
    l = line.strip().split() 
    if(not l[0] == oldKey):
        if(oldKey):
            print(oldKey+"\t"+(str(dMin) if dMin > -1 else 'INF')+"\t"+M)
        oldKey = l[0]
        dMin = -1
        M = '{}'
    if(l[2] == '{}'):
        if(l[1].isdigit() and (dMin < 0 or int(l[1]) < dMin)):
            dMin = int(l[1])
    else:
        M = l[2]
        if(l[1].isdigit() and (dMin < 0 or int(l[1]) < dMin)):
            dMin = int(l[1])
 
if(oldKey):  print(oldKey+"\t"+(str(dMin) if dMin > -1 else 'INF')+"\t"+M)

