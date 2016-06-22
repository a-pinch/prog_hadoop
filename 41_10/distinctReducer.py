#! /usr/bin/python3
import sys

oldKey = ''
for line in sys.stdin:
    key = line.strip().split("\t")[0]
    if(key != oldKey):
        print(key)
        oldKey = key
