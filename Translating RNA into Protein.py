#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:47:06 2024

@author: hngu
"""
f = open('/Users/hngu/Downloads/rosalind_prot.txt', 'r')
strand = f.readline()

codon = {
    'UCA': 'S',    # Serina
    'UCC': 'S',    # Serina
    'UCG': 'S',    # Serina
    'UCU': 'S',    # Serina
    'UUC': 'F',    # Fenilalanina
    'UUU': 'F',    # Fenilalanina
    'UUA': 'L',    # Leucina
    'UUG': 'L',    # Leucina
    'UAC': 'Y',    # Tirosina
    'UAU': 'Y',    # Tirosina
    'UAA': '*',    # Stop
    'UAG': '*',    # Stop
    'UGC': 'C',    # Cisteina
    'UGU': 'C',    # Cisteina
    'UGA': '*',    # Stop
    'UGG': 'W',    # Triptofano
    'CUA': 'L',    # Leucina
    'CUC': 'L',    # Leucina
    'CUG': 'L',    # Leucina
    'CUU': 'L',    # Leucina
    'CCA': 'P',    # Prolina
    'CCC': 'P',    # Prolina
    'CCG': 'P',    # Prolina
    'CCU': 'P',    # Prolina
    'CAC': 'H',    # Histidina
    'CAU': 'H',    # Histidina
    'CAA': 'Q',    # Glutamina
    'CAG': 'Q',    # Glutamina
    'CGA': 'R',    # Arginina
    'CGC': 'R',    # Arginina
    'CGG': 'R',    # Arginina
    'CGU': 'R',    # Arginina
    'AUA': 'I',    # Isoleucina
    'AUC': 'I',    # Isoleucina
    'AUU': 'I',    # Isoleucina
    'AUG': 'M',    # Methionina
    'ACA': 'T',    # Treonina
    'ACC': 'T',    # Treonina
    'ACG': 'T',    # Treonina
    'ACU': 'T',    # Treonina
    'AAC': 'N',    # Asparagina
    'AAU': 'N',    # Asparagina
    'AAA': 'K',    # Lisina
    'AAG': 'K',    # Lisina
    'AGC': 'S',    # Serina
    'AGU': 'S',    # Serina
    'AGA': 'R',    # Arginina
    'AGG': 'R',    # Arginina
    'GUA': 'V',    # Valina
    'GUC': 'V',    # Valina
    'GUG': 'V',    # Valina
    'GUU': 'V',    # Valina
    'GCA': 'A',    # Alanina
    'GCC': 'A',    # Alanina
    'GCG': 'A',    # Alanina
    'GCU': 'A',    # Alanina
    'GAC': 'D',    # Acido Aspartico
    'GAU': 'D',    # Acido Aspartico
    'GAA': 'E',    # Acido Glutamico
    'GAG': 'E',    # Acido Glutamico
    'GGA': 'G',    # Glicina
    'GGC': 'G',    # Glicina
    'GGG': 'G',    # Glicina
    'GGU': 'G'     # Glicina
}

def proteins(strand):
    aa = ''
    for i in range(0, len(strand), 3):
        #program ends when it reads a stop codon
        if codon[strand[i:i+3]] == '*':
            break
        aa += codon[strand[i:i+3]]
    print(aa)
        
proteins(strand)
    

