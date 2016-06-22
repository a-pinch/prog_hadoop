#! /usr/bin/python3
import sys

oldKey = ''
sum=cnt=0
for line in sys.stdin:
    l = line.strip().split("\t")
    value = l[1].strip().split(";")
    if l[0] == oldKey:
        sum = sum + int(value[0])
        cnt = cnt + 1
    else:
        if oldKey: print(oldKey+"\t"+str(sum)+";"+str(cnt))
        oldKey = l[0]
        sum = int(value[0])
        cnt = 1
if oldKey: print(oldKey+"\t"+str(sum)+";"+str(cnt))
       
