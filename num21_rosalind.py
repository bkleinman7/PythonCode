#suffix to prefix
import re
import operator
import numpy as np

with open("example.txt","r") as file:
    dna_string = []

    for dna in file:
        dna = dna.rstrip('\n');
        dna_string.append(dna)

for suffix_kmer in sorted(dna_string):
    for prefix_kmer in sorted(dna_string):
        if suffix_kmer[1:] == prefix_kmer[:-1]:
            print(suffix_kmer + " -> " + prefix_kmer)
