#! /usr/bin/python3
import sys,re

for line in sys.stdin:
    l = line.strip().split(":",1) 
    for w in re.compile("\W").split(l[1]):
        print(w+"#"+l[0]+"\t1")
    
