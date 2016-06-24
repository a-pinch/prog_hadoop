#! /usr/bin/python3
import sys,re

r = re.compile("\W+")
for line in sys.stdin:    
    l = line.strip().split() 
    print(l[0]+"\t"+l[1]+"\t"+l[2])
    n = 0.0;
    for e in r.split(l[2]):
        if(e): n+=1.0
    for e in r.split(l[2]):        
        if(e): print("%s\t%.3f\t{}" % (e, float(l[1])/n)) 
