import re
import sys
import operator

nucleotides = ['A', 'C', 'G','T']

def HammeringDistance(a, b):
    count = 0;
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return(count)

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    distance = 0
    size = len(Pattern)
    for j in range(len(Dna)):
        HammingDistance = float("inf")
        for i in range(len(Dna[0]) - size + 1):
            string_genome = Dna[j]
            kmer = string_genome[i:i+size]
            if HammingDistance > HammeringDistance(Pattern, kmer):
                HammingDistance = HammeringDistance(Pattern, kmer)
        distance += HammingDistance
    return distance

with open("example.txt","r") as file:
    Pattern = file.readline();
    Pattern = Pattern.rstrip('\n');

    for dna in file:
        dna = dna.split();

distance_ = DistanceBetweenPatternAndStrings(Pattern, dna);

print(distance_)
