#! /usr/bin/python3
import sys

def getMinEdge(q, d, w):
    "find short way to q edge"
    m = -1
    for c,k in d.items():
        if((c,q) in w):
            if(m < 0):
                m = k+w[(c,q)]
            else:
                if(k+w[(c,q)]<m):
                    m = k+w[(c,q)]
    return m

v = r = s = e = i = 0
w = {}
d = {}

for line in sys.stdin:    
    l = line.strip().split() 
    if(i == 0):
        v = int(l[0])
        r = int(l[1])
    else:
        if(i <= r):
            w[(int(l[0]),int(l[1]))] = int(l[2])
        else:
            s = int(l[0])
            e = int(l[1])
            d[s] = 0
    i+=1
while e not in d:
    mm = -1
    mi = e
    for i in range(v):
        if(i+1 not in d):
            m = getMinEdge(i+1, d, w)
            if(m>-1 and (m<mm or mm<0)):
                mm = m
                mi = i+1
    d[mi] = mm
print(d[e])
