import re

with open("example.txt","r") as file:
    text_file = open("Output.txt", "w")
    dna = file.readline();
    dna = dna.rstrip('\n');
    integers = file.readline();
    index = 0;

    for s in re.findall(r'\d+', integers):
        if index == 0:
            size = int(s);
        elif index == 1:
            length_of_scan = int(s);
        elif index == 2:
            min_occur = int(s);
        index += 1

    myList = [];

    for i in range(0,(len(dna)-length_of_scan)):
        count = 1;
        newdict = {}
        for j in range(i,length_of_scan+i):
            dna = list(dna)
            kmer = ''.join(dna[j:j+size])

            if kmer in newdict.keys():
                #print(newdict)
                newdict[kmer] += 1;
                if newdict[kmer] >= min_occur:
                    #print(kmer)
                    if kmer not in myList:
                        myList.append(kmer);
            else:
                newdict[kmer] = count;
                #print(kmer)

    i = 0
    for l in myList:
        text_file.write(myList[i])
        i += 1
    print(myList)