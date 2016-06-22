#! /usr/bin/python3
import sys

for line in sys.stdin:
    items = line.strip().split(" ")
    for i in items :
        H= {}
        for j in items:
            if(i != j): 
                if(j in H): H[j] = H[j] + 1
                else: H[j] = 1
        print(i+"\t"+", ".join(k+":"+str(v) for k,v in H.items()))
