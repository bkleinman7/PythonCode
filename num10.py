import re

NumberToSymbol = {0:'A', 1:'C', 2:'G', 3:'T'}

def NumberToPattern(index, k):
    k = int(k)
    index = int(index)
    if k == 1:
        return NumberToSymbol[index]
    
    prefixIndex = index / 4
    prefixIndex = int(prefixIndex)
    r = index % 4
    PrefixPattern = NumberToPattern(prefixIndex, (k - 1))
    return (PrefixPattern + NumberToSymbol[r])


with open("example.txt","r") as file:
    text_file = open("Output.txt", "w")
    index = file.readline();
    k = file.readline();
    result = NumberToPattern(index, k);
    print(result)
    text_file.write(NumberToPattern(index, k))
    text_file.close()