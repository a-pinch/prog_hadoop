#! /usr/bin/python3
import sys

H= {}
oldLine = ''
for line in sys.stdin:
    if(line != oldLine):
        oldLine = line
        key = line.strip().split("\t")[1]
        if(key in H): H[key] = H[key] + 1
        else: H[key] = 1
for k,v in H.items():
    print(k+"\t"+str(v))
