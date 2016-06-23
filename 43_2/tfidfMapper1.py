#! /usr/bin/python3
import sys,re

for line in sys.stdin:
    l = line.strip().split(":",1) 
    r = re.compile("\W+")
    for w in r.split(l[1]):
        if(w):  print(w+"#"+l[0]+"\t1")
    
