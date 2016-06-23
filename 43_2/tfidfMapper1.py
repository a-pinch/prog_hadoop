#! /usr/bin/python3
import sys

for line in sys.stdin:
    l = line.strip().split(":") 
    for w in l[1].strip().split(" "):
        print(w+"#"+l[0]+"\t1")
    
