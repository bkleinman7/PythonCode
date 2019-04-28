import re

with open("example.txt","r") as file:
    text_file = open("Output.txt", "w")
    dna = file.readline();
    totalList = [];
    count = 0;
    for l in dna:
        if(l == "C"):
            count -= 1
        if(l == "G"):
            count += 1
        totalList.append(count)

    smallest = min(totalList);
    min_ind = [];
    for index, element in enumerate(totalList):
        if smallest == element:
            min_ind.append(index)
    #print(min_ind)
    i = 0
    for l in min_ind:
        text_file.write(str(min_ind[i])+ ' ')
        i += 1
    text_file.close()