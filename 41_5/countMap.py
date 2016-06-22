#! /usr/bin/python3
import sys

H = {}

for line in sys.stdin:
    for token in line.strip().split(" "):        
        if token: 
            if token in H: H[token] = H[token] + 1
            else: H[token] = 1
for k,v in H.items():        
    print(k + "\t" +str(v))
