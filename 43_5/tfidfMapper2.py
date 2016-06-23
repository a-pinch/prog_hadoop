#! /usr/bin/python3
import sys

for line in sys.stdin:
    l = line.strip().split("\t") 
    print(l[0]+"\t"+l[1]+";"+l[2]+";1")

