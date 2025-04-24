#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 12:07:49 2024

@author: hngu
"""

print("Directionality will be the same as the template strand provided.")
s = input("Template Strand: ")
r = ""
i = 0

# Reverse original strand
s = s[::-1]

# Make reverse complement by reading through each nucleotide
# in original strand and adding its complement to r
while i < len(s):
    if s[i] == "A":
        r += "T"
        i += 1
    
    elif s[i] == "T":
        r += "A"
        i += 1
    
    elif s[i] == "G":
        r += "C"
        i += 1
    
    elif s[i] == "C":
        r += "G"
        i += 1

print(f'Reverse Complement: {r[::-1]}')