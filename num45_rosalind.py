def HammeringDistance(a, b):
    count = 0;
    for x, y in zip(a, b):
        if x != y:
            count += 1
    return(count)

#Gather all patterns
with open('example.txt') as file:
    i = 0
    new_patterns = []
    patterns = []
    sub_patterns = []
    for line in file:
        if i == 0:
            patterns = line.strip()
        else:
            sub_patterns = line.split(' ')
        i += 1

int_array = []
d = 2
size_array = []
for k in sub_patterns:
    if len(k) not in size_array:
        size_array.append(len(k))
print(size_array)
'''for j in sub_patterns:
    size = len(j)
    for i in range(len(patterns) - size + 1):
        pattern_k = patterns[i:i+size]
        count = HammeringDistance(j, pattern_k)
        if count <= d:
            #print(j, pattern_k, i)
            int_array.append(i)
    
final_string = ""
for i in sorted(int_array):
    final_string += str(i) + ' '
print(final_string)'''
