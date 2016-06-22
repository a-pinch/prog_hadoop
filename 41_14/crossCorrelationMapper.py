#! /usr/bin/python3
import sys

H= {}
oldLine = ''
for line in sys.stdin:
    items = line.strip().split(" ")
    for i in items :
        for j in items:
            if(i != j): print(str(i)+","+str(j)+"\t1")
