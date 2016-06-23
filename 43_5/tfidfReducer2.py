#! /usr/bin/python3
import sys

oldKey = ''
c = 0
H = {}
for line in sys.stdin:
    l = line.strip().split() 
    m = l[1].split(";")
    if(oldKey == l[0]): 
        c+=int(m[2])
    else: 
        if(c):
            for k,v in H.items():
                print(k+"\t"+v+"\t"+str(c))
            H = {} 
        c = 1
    oldKey = l[0]
    H[l[0]+"#"+m[0]] = m[1]
#    print(H)    
if(c): 
    for k,v in H.items():
        print(k+"\t"+v+"\t"+str(c))

