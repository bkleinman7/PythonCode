import re
import operator
import numpy as np

nucleotides = ['A', 'C', 'G','T']
profile_matrix = []

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
        dna_string.append(dna)


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
def score(kmer_array_):
    maxCount = 0.0

    for k in range(len(kmer_array_)):
        t = []
        for i in range(size_kmer):
            kmer_input = kmer_array_[k]
            if kmer_input[i] == 'A':
                t.append(profile_matrix[0][i])
            if kmer_input[i] == 'C':
                t.append(profile_matrix[1][i])
            if kmer_input[i] == 'G':
                t.append(profile_matrix[2][i])
            if kmer_input[i] == 'T':
                t.append(profile_matrix[3][i])

        maxCount += np.prod(np.array(t))

    return maxCount

BestMotif = []

#Create first appearing kmer in each string
for j in range(num_kmers):
    for i in range(1):
        string_genome = dna_string[j]
        kmer = string_genome[i:size_kmer]
        BestMotif.append(kmer)


#Loop through first string of dna
for i in range(len(dna_string[0]) - size_kmer + 1):
    motif = []
    Profile_Matrix = []
    profile_matrix = []
    string_genome = dna_string[0]
    kmer_ = string_genome[i:i+size_kmer]
    motif.append(kmer_)
    j = 1
    Profile_Matrix.append(kmer_)
    profile_matrix = create_matrix_prof(Profile_Matrix, j)
    for j in range(1, num_kmers):
        maxKmer = 0
        maxKmer_Map = {}
        kmer_array_test = []
        for k in range(len(dna_string[0]) - size_kmer + 1):
            kmer_array_test = []
            kmerCount = 0
            string_genome = dna_string[j]
            kmer = string_genome[k:k+size_kmer]
            kmer_array_test.append(kmer)
            kmerCount = score(kmer_array_test)
            if kmerCount > maxKmer:
                maxKmer = kmerCount
                maxKmer_Map[kmer] = maxKmer
        j += 1
        if len(maxKmer_Map) > 0:
            kmer = max(maxKmer_Map, key=maxKmer_Map.get)
            motif.append(kmer)
            Profile_Matrix.append(kmer)
            profile_matrix = create_matrix_prof(Profile_Matrix, j)
        else:
            kmer = string_genome[0:0+size_kmer]
            motif.append(kmer)
            Profile_Matrix.append(kmer)
            profile_matrix = create_matrix_prof(Profile_Matrix, j)

    if Score(motif) < Score(BestMotif):
        BestMotif = motif

for row in BestMotif:
    print(row, end = '\n')
    text_file.writelines(row + ' ')

text_file.close()
