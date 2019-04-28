import re

def compare(a, b):
    count = 0;
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return(count)

with open("example.txt","r") as file:
    text_file = open("Output.txt", "w")
    dna_string = file.readline();
    dna_string = dna_string.rstrip('\n');
    string_patter_len = len(dna_string)
    text = file.readline();
    text = text.rstrip('\n');
    d = file.readline();
    myList = [];
    for i in range(0,len(text)-string_patter_len+1):
        text = list(text)
        kmer = ''.join(text[i:i+string_patter_len])
        total = compare(kmer, dna_string)
        if total <= int(d):
            myList.append(i);
    #print(myList)

    i = 0
    for l in myList:
        text_file.write(str(myList[i]) + ' ')
        i += 1
    text_file.close()