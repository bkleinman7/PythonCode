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

    for dna in file:
        #dna = file.readline();
        dna = dna.rstrip('\n');
        dna_string.append(dna)

#text_file = open("Output.txt", "w")

length_ = len(dna_string[0])
output_map = {}
total_value = []
minC = 0

for j in range(len(dna_string)):
    for i in range(length_ - size + 1):
        string_genome = dna_string[j]
        kmer = string_genome[i:i+size]
        total_count = 0
        for a in range(len(dna_string)):
            del total_value[:]
            for b in range(length_ - size + 1):
                string_genome = dna_string[a]
                kmer_pattern = string_genome[b:b+size]
                total = compare(kmer_pattern, kmer)
                total_value.append(total)
                #print(kmer, total, a)
            total_count = min(total_value) + total_count

        output_map[kmer] = total_count


print(minC)
print(output_map)
print(min(output_map, key=output_map.get))
#for l in output:
    #text_file.writelines(l + ' ')

#text_file.close()
