#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 14:42:07 2024

@author: hngu
"""

# The ID of the string having the highest GC-content, 
# followed by the GC-content of that string. 
# Rosalind allows for a default error of 0.001 in all 
# decimal answers unless otherwise stated
f = open('rosalind_gc.txt', 'r')
s = []
rosalind = []
i = 0
t = 0
p = 0
g = f.readlines()

while len(g) > 0:

    for line in g:
        if ">" in line:
            if line not in rosalind: 
                rosalind.append(line)
            t += 1
        if t > 1:
            break
        s.append(line)
    print(len(s))
    
    h = ''.join(s[1:len(s)])
    h = h.replace("\n", "")
    print(h)
    
    #n is variable keeping track of which string has the highest G/C con
    l = len(h)
    a = h.count("G")
    b = h.count("C") 
            
    print(round(((a+b)/l)*100, 6), "%")
    if round(((a+b)/l)*100, 6) > p:
        p = round(((a+b)/l)*100, 6)
        n = i
    i += 1

    del g[0:len(s)]
    s = []
    t = 0

print(rosalind[n][1:])
print(p)
    

        
    
    
# for line in f:
#     if ("G" or "C" or "A" or "T") in line:
        
    
# s = f.readlines()[1::2]
# i = 0

# #n is variable keeping track of which string has the highest G/C con
# while i < len(s):
#     l = len(s[i])
#     a = s[i].count("G")
#     b = s[i].count("C") 
        
#     if i == 0 or round(((a+b)/l)*100, 6) > p:
#         p = round(((a+b)/l)*100, 6)
#         n = i
           
#     i += 1

# f = open('rosalind_gc.txt', 'r')
# g = f.readlines()
# h = g.index(s[n])

# print(g[h-1])
# print(p)

    
