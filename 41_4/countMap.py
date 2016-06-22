#! /usr/bin/python3
import sys

for line in sys.stdin:
    H = {}
    for token in line.strip().split(" "):        
        if token: 
            if token in H: H[token] = H[token] + 1
            else: H[token] = 1
    for k,v in H.items():        
        print(k + "\t" +str(v))
