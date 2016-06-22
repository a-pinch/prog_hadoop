#! /usr/bin/python3
import sys

oldKey = ''
H = {}
for line in sys.stdin:
    l = line.strip().split("   ") 
    m = l[1].strip().split(":")
    if(l[0] != oldKey):
        if('query' in H):
            for q in H['query']:
                if('url' in H):
                    for u in H['url']:
                        print(oldKey + "\t" + q + "\t" + u)
        H = {}
        oldKey = l[0]
    if(m[0] in H): H[m[0]].append(m[1])
    else: H[m[0]] = [m[1]]
if('query' in H):        
    for q in H['query']:
        if('url' in H):
            for u in H['url']:
                print(oldKey + "\t" + q + "\t" + u)
