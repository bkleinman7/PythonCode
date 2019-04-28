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
        if dna not in motif:
            motif.append(dna)

text_file = open("Output.txt", "w")

found = 0
must_find = len(motif) - 1
print(must_find)

new_string = ""
new_kmer = ""
start_kmer = ""
unsuccsessful_kmers = []
success_kmer = []
max_found = 0
j = 0

for kmer in motif:
    j += 1
    found = 0
    new_kmer = ""
    new_string = ""
    i = 0
    print(j)
    while(True):
        for kmer2 in motif:
            if new_kmer == "":
                suffix = kmer[1:]
            else:
                suffix = new_kmer[1:]
            prefix = kmer2[:-1]
            if suffix == prefix:
                i += 1
                found += 1
                if found == 1:
                    start_kmer = kmer
                    new_string += kmer + kmer2[len(kmer2)-1:]
                    new_kmer = kmer2
                else:
                    new_string += kmer2[len(kmer2)-1:]
                    new_kmer = kmer2
        if i == 0:
            break
        i = 0
        if found == must_find:
            print("FOUND IT!", new_string)
            break

text_file.close()
