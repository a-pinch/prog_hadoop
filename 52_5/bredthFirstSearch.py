#! /usr/bin/python3
import sys,re

r = re.compile("\W+")
for line in sys.stdin:    
    l = line.strip().split() 
    print(l[0]+"\t"+l[1]+"\t"+l[2])
    for e in r.split(l[2]):
        if(e): print(e+"\t"+(str(int(l[1])+1) if l[1].isdigit() else l[1])+"\t{}")
