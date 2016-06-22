#! /usr/bin/python3
import sys

for line in sys.stdin:
    l = line.strip().split("\t")
    for g in l[1].strip().split(","):
        print(l[0]+","+g+"\t1"); 
