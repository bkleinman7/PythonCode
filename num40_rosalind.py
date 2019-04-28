with open('example.txt') as file:
    i = 0
    patterns = []
    text_line = ""
    for line in file:
        if i == 0:
            text_line = line.strip()
        else:
            patterns.append(line.strip())
        i += 1

int_array = []

size = len(patterns[0])
for i in range(len(text_line) - size + 1):
    pattern_k = text_line[i:i+size]
    for l in patterns:
        if pattern_k == l:
            int_array.append(i)

final_string = ""
for i in int_array:
    final_string += str(i) + ' '
print(final_string)
                
