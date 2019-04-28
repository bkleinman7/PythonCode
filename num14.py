import re
import operator
import numpy as np

nucleotides = ['A', 'C', 'G','T']
profile_matrix = []

def compare(a, b):
    count = 0;
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return(count)

with open("example.txt","r") as file:
    dna_string = file.readline();
    dna_string = dna_string.rstrip('\n');
    length_kmer = file.readline();
    length_kmer = length_kmer.rstrip('\n');
    length_kmer = int(length_kmer)

    for line in file:
        number = line.split();
        profile_matrix.append(number)

text_file = open("Output.txt", "w")

test_array = []
kmer = ""
map_kmer = {}
max_value = 0.000000

def profile_matrix_def(kmer_input):
    maxCount = 0.0
    t = []
    for i in range(length_kmer):

        if kmer_input[i] == 'A':
            profile_matrix[0][i] = float(profile_matrix[0][i])
            t.append(profile_matrix[0][i])
        if kmer_input[i] == 'C':
            profile_matrix[1][i] = float(profile_matrix[1][i])
            t.append(profile_matrix[1][i])
        if kmer_input[i] == 'G':
            profile_matrix[2][i] = float(profile_matrix[2][i])
            t.append(profile_matrix[2][i])
        if kmer_input[i] == 'T':
            profile_matrix[3][i] = float(profile_matrix[3][i])
            t.append(profile_matrix[3][i])
    print(sum(t))
    return maxCount




for i in range(len(dna_string) - length_kmer + 1):
    kmer = dna_string[i:i+length_kmer]
    total_max_value = profile_matrix_def(kmer)
    if total_max_value > max_value:
        max_value = total_max_value
        map_kmer[kmer] = max_value

print(max(map_kmer, key=map_kmer.get))

text_file.close()
