#! /usr/bin/python3
import sys

oldKey = ''
oldValue = ''
for line in sys.stdin:
    l = line.strip().split()
    if(l[0] == oldKey):
        if(l[1] != oldValue):
            print(l[0])            
    else: oldKey = l[0]
    oldValue = l[1]
