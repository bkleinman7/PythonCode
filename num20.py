import re
import operator
import numpy as np
import random
import sys

#Different from just random noise

nucleotides = ['A', 'C', 'G','T']
profile_matrix = []

with open("example.txt","r") as file:
    integers = file.readline();
    integers = integers.rstrip('\n');
    index = 0;
    dna_string = []

    for dna in file:
        if not dna.startswith('>'):
            dna = dna.rstrip('\n');
            dna_string.append(dna)

test_second_map = {}

for int_size_kmer in range(4,len(dna_string)):
    test_map = {}
    size_kmer = int_size_kmer
    num_kmers = len(dna_string)


    text_file = open("Output.txt", "w")

    test_array = []
    kmer = ""
    map_kmer = {}
    max_value = 0.000000

    def Consensus(Motifs):
    	k = len(Motifs[0])
    	count = Count(Motifs)
    	consensus=""
    	for j in range(k):
    		m=0
    		frequentSymbol = ""
    		for symbol in "ACGT":
    			if count[symbol][j] > m:
    				m = count[symbol][j]
    				frequentSymbol = symbol
    		consensus+=frequentSymbol
    	return consensus

    def Count(Motifs):
    	count = {}
    	k = len(Motifs[0])
    	for symbol in "ACGT":
    			count[symbol]=[]
    			for i in range(k):
    				count[symbol].append(0)
    	t = len(Motifs)
    	for i in range(t):
    		for j in range(k):
    			symbol = Motifs[i][j]
    			count[symbol][j] += 1
    	return count

    def Score(Motifs):
    	consensus=Consensus(Motifs)
    	count= Count(Motifs)
    	k =len(consensus)
    	j= len(count)
    	t=len(Motifs)
    	mscore = 0
    	score =-1
    	for i in range(k):
    		mscore= t - count[consensus[i]][i]
    		score += mscore
    	return score

    def create_matrix_prof(profile_array, j):
        Test_Prof_array = []
        Test_Prof_matrix = []
        for k in range(size_kmer):
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

    def repeatedRandomizedMotifSearch(k, t, dna):
        bestScore = float('inf')
        bestMotifs = []
        i = 0
        while True:
            motifs = randomizedMotifSearch(k,t,dna)
            score = Score(motifs)
            if score < bestScore:
                bestScore = score
                bestMotifs = motifs
                i = 0
            else:
                i += 1
            if i > 100:
                break
        return bestMotifs

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

    def randomizedMotifSearch(k, t, dna):
        bestMotifs = randomMotifs(dna,k)
        bestScore = Score(bestMotifs)
        while True:
            profile = create_matrix_prof(bestMotifs,t)
            motifs = motifsFromProfile(dna,k,t,profile)
            score = Score(motifs)
            if score < bestScore:
                bestMotifs = motifs
                bestScore = score
            else:
                return bestMotifs

    def randomMotifs(dna, k):
        return [randomKmer(seq,k) for seq in dna]

    def randomKmer(seq, k):
        start = random.randint(0, len(seq)-k)
        return seq[start:start+k]

    def HammeringDistance(a, b):
        count = 0;
        for x, y in zip(a, b):
            if x != y:
                count += 1
        return(count)

    bestMotifs = repeatedRandomizedMotifSearch(size_kmer,num_kmers,dna_string)

    print("Motif formed from profile:")
    test_prof = create_matrix_prof(dna_string, len(dna_string))
    motifs = motifsFromProfile(dna_string,size_kmer,len(dna_string),test_prof)

    lowest_score = 4

    i = 0
    best_level = []
    for l in motifs:
        i += 1
        for j in bestMotifs:
            score = HammeringDistance(l,j)
            if score < lowest_score:
                lowest_score = score
                #print(i, l, score)
                best_level.append(i)
                '''if l in test_map.keys():
                    test_map[l] += 1
                else:
                    test_map[l] = 1'''
                if i == 5:
                    print("Rv0081", l)
                if i in test_second_map.keys():
                    test_second_map[i] += 1
                else:
                    test_second_map[i] = 1
    if not test_second_map == False:
        print(test_second_map)
        text_file.write(str(test_second_map))
    #if not test_map == False:
        #print(max(test_map, key=test_map.get))
        #text_file.write(str(max(test_map, key=test_map.get)))
    text_file.close()
