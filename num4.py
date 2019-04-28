import re

with open("example.txt","r") as file:
    text_file = open("Output.txt", "w")
    amino = file.readline();
    amino = amino.rstrip('\n');
    size = file.readline();
    size = int(size)

myMap = {}
maxC = 0
for i in range(0,len(amino)-size+1):
    kmer = amino[i:i+size]
    if kmer in myMap.keys():
        myMap[kmer] += 1
        if myMap[kmer] > maxC:
            maxC = myMap[kmer]
    else:
        myMap[kmer] = 1

for l in myMap:
    if myMap[l] == maxC:
        print(l)

text_file.close()
