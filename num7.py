import re

def compare(a, b):
    count = 0;
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return(count)

with open("example.txt","r") as file:
    text_file = open("Output.txt", "w")
    dna_num_one = file.readline();
    dna_num_two = file.readline();
    total = compare(dna_num_one, dna_num_two)
    text_file.write(str(total))
    text_file.close()
