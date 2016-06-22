#! /usr/bin/python3
import sys

for line in sys.stdin:
    l = line.strip().split()
    if(l[1] == 'user10'):
        print(line, end="") 
