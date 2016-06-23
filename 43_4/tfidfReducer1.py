#! /usr/bin/python3
import sys

oldKey = ''
c = 0
for line in sys.stdin:
    l = line.strip().split() 
    if(oldKey == l[0]): c+=1
    else: 
        if(c):
            k = oldKey.split("#")
            print(k[0]+"\t"+k[1]+"\t"+str(c))
        c = 1
    oldKey = l[0]
if(c):  
    k = oldKey.split("#")
    print(k[0]+"\t"+k[1]+"\t"+str(c))

