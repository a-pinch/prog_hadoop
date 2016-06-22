#! /usr/bin/python3
import sys

H = {}
oldKey = ''
sum=cnt=0
for line in sys.stdin:
    l = line.strip().split("\t")
    if l[0] == oldKey:
        sum = sum + int(l[1])
        cnt = cnt + 1
    else:
        if oldKey: print(oldKey+"\t"+str(sum/cnt))
        oldKey = l[0]
        sum = int(l[1])
        cnt = 1
if oldKey: print(oldKey+"\t"+str(sum/cnt))
       
