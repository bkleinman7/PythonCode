def MapLastToFirst(LastColumn):
    FirstColumn = sorted(LastColumn)
    map_index = []
    for char in LastColumn:
        index = FirstColumn.index(char)
        #print(index)
        map_index.append(index)
        FirstColumn[index] = "#"
    return(map_index)


def BWMatching(FirstColumn, LastColumn, Pattern, LastToFirst):
    top = 0
    bottom = (len(LastColumn) - 1)
    while top <= bottom:
        if Pattern:
            symbol = Pattern[-1]
            Pattern = Pattern[:-1]
            last_short = LastColumn[top : (bottom + 1)]
            if symbol in last_short:
                topIndex  = last_short.index(symbol) + top
                bottomIndex = len(last_short) - last_short[::-1].index(symbol) + top - 1
                top = LastToFirst[topIndex]
                bottom = LastToFirst[bottomIndex]
            else:
                return(0)
        else:
            return(bottom - top + 1)

with open('example.txt') as file:
    i = 0
    LastColumn = ""
    patterns = []
    for line in file:
        if i == 0:
            LastColumn = line.strip()
        else:
            patterns = line.split(' ')
        i += 1

FirstColumn = sorted(LastColumn)
LastToFirst = MapLastToFirst(LastColumn)
matches = []

for pattern in patterns:
    matches.append(BWMatching(FirstColumn, LastColumn, pattern, LastToFirst))

string_int = ""

for i in matches:
    string_int += str(i) + ' '

print(string_int)
