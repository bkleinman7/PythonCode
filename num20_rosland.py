import re
import operator
import numpy as np

#sequencing depth of 30 reads

with open("example.txt","r") as file:
    integers = file.readline();
    integers = integers.rstrip('\n');
    index = 0;
    dna_string = []

    #gather size of kmer and hammering distance
    for s in re.findall(r'\d+', integers):
        if index == 0:
            size_kmer = int(s);
        elif index == 1:
            num_kmers = int(s);
        index += 1

    for dna in file:
        dna = dna.rstrip('\n');

motif = []

for i in range(len(dna) - size_kmer + 1):
    kmer_ = dna[i:i+size_kmer]
    motif.append(kmer_)

print(motif)

for sorted_kmer in sorted(motif):
    print(sorted_kmer)
