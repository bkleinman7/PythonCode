import re
import operator

nucleotides = ['A', 'C', 'G','T']
success = []

def compare(a, b):
    count = 0;
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return(count)

with open("example.txt","r") as file:
    integers = file.readline();
    integers = integers.rstrip('\n');
    index = 0;
    dna_string = []

    #gather size of kmer and hammering distance
    for s in re.findall(r'\d+', integers):
        if index == 0:
            size = int(s);
        elif index == 1:
            hammer_distance = int(s);
        index += 1

    for dna in file:
        #dna = file.readline();
        dna = dna.rstrip('\n');
        dna_string.append(dna)

text_file = open("Output.txt", "w")

length_ = len(dna_string[0])
output = []
output_found = []

for j in range(len(dna_string)):
    for i in range(length_ - size + 1):
        string_genome = dna_string[j]
        kmer = string_genome[i:i+size]
        for x in range(size):
            temp = kmer
            for d in range(4):
                temp = temp[:x] + nucleotides[d] + temp[x + 1:]
                #new line of each string
                found_kmer = 0
                count_to_four = 0
                add_kmer = False
                output_found[:] = []
                for a in range(len(dna_string)):
                    found_kmer = 0
                    for b in range(length_ - size + 1):
                        string_genome = dna_string[a]
                        kmer = string_genome[b:b+size]
                        total = compare(temp, kmer)
                        if(total <= hammer_distance):
                            if a not in output_found:
                                output_found.append(a)
                        if(len(output_found) == len(dna_string)):
                            if temp not in output:
                                output.append(temp)


for l in output:
    text_file.writelines(l + ' ')

text_file.close()
