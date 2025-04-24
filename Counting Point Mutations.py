#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 13:34:35 2024

@author: hngu
"""
f = open('/Users/hngu/Downloads/rosalind_hamm.txt', 'r')
s = f.readline()
t = f.readline()
i = 0
h = 0

while i < len(s): 
    if s[i] != t[i]:
        h += 1
    i += 1

print(h)

