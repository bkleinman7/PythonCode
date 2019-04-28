import re

nucleotides = ['A', 'C', 'G','T']
success = []

def compare(a, b):
    count = 0;
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return(count)


with open("example.txt","r") as file:
    text_file = open("Output.txt", "w")
    Pattern = file.readline();
    d = file.readline();
    for x in range(0, len(Pattern)-1):
        temp = Pattern
        print(x)
        temp = temp[:x] + nucleotides[0] + temp[x + 1:]
        total = compare(temp, Pattern)
        if(total <= d and temp != Pattern):
            success.append(temp)
        print(temp)
        temp = temp[:x] + nucleotides[1] + temp[x + 1:]
        total = compare(temp, Pattern)
        if(total <= d and temp != Pattern):
            success.append(temp)
        print(temp)
        temp = temp[:x] + nucleotides[2] + temp[x + 1:]
        total = compare(temp, Pattern)
        if(total <= d and temp != Pattern):
            success.append(temp)
        print(temp)
        temp = temp[:x] + nucleotides[3] + temp[x + 1:]
        total = compare(temp, Pattern)
        if(total <= d and temp != Pattern):
            success.append(temp)
        print(temp)
    success.append(Pattern)
    print(success)
    for l in success:
        print(l)
        text_file.write(l)
    text_file.close()
