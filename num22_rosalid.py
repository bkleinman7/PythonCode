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

    motif = []

    for dna in file:
        dna = dna.rstrip('\n');
        motif.append(dna)

'''for i in range(len(dna) - size_kmer + 1):
    kmer_ = dna[i:i+size_kmer]
    motif.append(kmer_)'''

text_file = open("Output.txt", "w")

map_kmer = {}

for kmer in sorted(motif):
    prefix_ = kmer[:-1]
    suffix_ = kmer[1:]
    if prefix_ in map_kmer.keys():
        map_kmer[prefix_] += "," + suffix_
    else:
        map_kmer[prefix_] = suffix_
    #print(prefix_ + " -> " + suffix_)

for l in map_kmer:
    #print(l + " -> " + map_kmer[l] + "\n")
    text_file.writelines(l + " -> " + map_kmer[l] + "\n")

text_file.close()
