#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 16:22:47 2024

@author: hngu
"""
f = open('rosalind_cons.txt', 'r')
h = f.readlines()
s = []
n = 0
a = "A: "
c = "C: "
g = "G: "
t = "T: "

for line in h:
    if ">" not in line:
        line.strip()
        s.append(line)
    
for i in range(0, len(s)):
    for i in range(0, len(s[i])):
        pass
    
a += str(s[1].count("A"))
c += str(s[1].count("C"))
g += str(s[1].count("G"))
t += str(s[1].count("T"))
    
    
print(a)
print(c)
print(g)
print(t)

    
