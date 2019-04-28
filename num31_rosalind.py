f = open("example.txt", "r")

dna = f.readline().strip()
pattern = f.readline().strip()

f.close()

map = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
       "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
       "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
       "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
       "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
       "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
       "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
       "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
       "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
       "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
       "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
       "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
       "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
       "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
       "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
       "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}

complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}

def returnPattern(kmer):
    k = 3
    j = 1
    new_kMers = []
    amino_string = ""
    run_size = int(len(kmer)/3)
    for i in range(run_size):
        new_kMers.append(kmer[i*k:j*k])
        j += 1

    for kmer in new_kMers:
        if kmer in map.keys():
            if map[kmer] == "STOP":
                break
            amino_string += map[kmer]

    return(amino_string)

k = (3*len(pattern))

for i in range(len(dna) - k + 1):
    kmer = dna[i:i+k]
    kmer_rna = kmer.replace('T', 'U')
    reverse_complement = "".join(complement.get(base, base) for base in reversed(kmer))
    kmer_rev_rna = reverse_complement.replace('T', 'U')
    if(returnPattern(kmer_rev_rna) == pattern or returnPattern(reverse_complement) == pattern or returnPattern(kmer_rna) == pattern or returnPattern(kmer) == pattern):
        print(kmer)
    #print(i, kmer, kmer_rna, reverse_complement, kmer_rev_rna)
