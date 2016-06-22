#! /usr/bin/python3
import sys

oldKey = ''
oldValue = ''
n = 0
for line in sys.stdin:
    l = line.strip().split()
    if(l[0] == oldKey):
        n += 1
    else:
        if(n == 1 and oldValue == 'A'):
            print(oldKey)            
        n = 1
    oldKey = l[0]
    oldValue = l[1]
if(n == 1 and oldValue == 'A'):
    print(oldKey)   
