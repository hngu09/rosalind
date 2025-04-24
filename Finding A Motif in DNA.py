#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 15:18:49 2024

@author: hngu
"""

f = open('/Users/hngu/Downloads/rosalind_subs.txt', 'r')
s = f.readline()
s = s.strip()
i = f.readline()
i = i.strip()

def motif(strand, index):
        #chop up strand into len(index) char strings
        #program runs through each one looking for index
        n = ''
        for j in range(0, len(strand)):
            if strand[j:j+len(index)] == index:
                n += str(j+1) + ' '
        print(n)
        
motif(s,i)