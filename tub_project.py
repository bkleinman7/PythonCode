import re
import operator
import numpy as np
import random
import sys

#Different from just random noise
nucleotides = ['A', 'C', 'G','T']
profile_matrix = []

with open("most_probable.txt","r") as file:
    dna_string = []

    for dna in file:
            dna = dna.rstrip('\n');
            dna_string.append(dna)

    size_kmer = 17
    num_kmers = len(dna_string)

text_file = open("Output.txt", "w")

def create_matrix_prof(profile_array, j):
    Test_Prof_array = []
    Test_Prof_matrix = []
    for k in range(3):
        count_a = 1
        count_c = 1
        count_g = 1
        count_t = 1
        Test_Prof_array = []
        for l in range(len(profile_array)):
            #print(profile_array[l][0])
            if profile_array[l][k] == 'A':
                count_a += 1
            if profile_array[l][k] == 'C':
                count_c += 1
            if profile_array[l][k] == 'G':
                count_g += 1
            if profile_array[l][k] == 'T':
                count_t += 1
        Test_Prof_array.append(count_a/j)
        Test_Prof_array.append(count_c/j)
        Test_Prof_array.append(count_g/j)
        Test_Prof_array.append(count_t/j)
        Test_Prof_matrix.append(Test_Prof_array)
    Test_PROF_M = []
    for u in range(len(nucleotides)):
        Test_PROF_A = []
        for t in range(size_kmer):#col
            Test_PROF_A.append(Test_Prof_matrix[t][u])
        Test_PROF_M.append(Test_PROF_A)
    return Test_PROF_M

#For creating a new profile count with each iteration
def score(kmer_array_, profile):
    maxCount = 0.0

    for k in range(len(kmer_array_)):
        t = []
        for i in range(size_kmer):
            kmer_input = kmer_array_[k]
            if kmer_input[i] == 'A':
                t.append(profile[0][i])
            if kmer_input[i] == 'C':
                t.append(profile[1][i])
            if kmer_input[i] == 'G':
                t.append(profile[2][i])
            if kmer_input[i] == 'T':
                t.append(profile[3][i])

        maxCount += np.prod(np.array(t))

    return maxCount

def motifsFromProfile(dna,size_kmer,num_kmers,profile):
    motif = []
    for j in range(0, num_kmers):
        maxKmer = 0
        maxKmer_Map = {}
        kmer_array_test = []
        for k in range(len(dna[0]) - size_kmer + 1):
            kmer_array_test = []
            kmerCount = 0
            string_genome = dna[j]
            kmer = string_genome[k:k+size_kmer]
            kmer_array_test.append(kmer)
            kmerCount = score(kmer_array_test, profile)
            if kmerCount > maxKmer:
                maxKmer = kmerCount
                maxKmer_Map[kmer] = maxKmer
        j += 1
        if len(maxKmer_Map) > 0:
            kmer = max(maxKmer_Map, key=maxKmer_Map.get)
            motif.append(kmer)
        else:
            kmer = string_genome[0:0+size_kmer]
            motif.append(kmer)
    return motif

print("Motif formed from profile:")
test_prof = create_matrix_prof(dna_string, len(dna_string))
motifs = motifsFromProfile(dna_string,size_kmer,len(dna_string),test_prof)

lowest_score = float('inf')

'''for l in motifs:
    for j in bestMotifs:
        score = HammeringDistance(l,j)
        if score < lowest_score:
            lowest_score = score
            print(l, score)

for row in bestMotifs:
    print(row, end = '\n')
    text_file.writelines(row + ' ')'''

text_file.close()
