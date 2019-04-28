SymbolToNumber = {'A':0, 'C':1, 'G':2, 'T':3}

def PatternToNumber(Pattern):

    if not Pattern:
        return 0
    print(Pattern[:-1])
    print(SymbolToNumber[Pattern[-1]])

    return 4 * PatternToNumber(Pattern[:-1]) + SymbolToNumber[Pattern[-1]]


with open("example.txt","r") as file:
    text_file = open("Output.txt", "w")
    dna = file.readline();
    text_file.write(str(PatternToNumber(dna)))
    text_file.close()