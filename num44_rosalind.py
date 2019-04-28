#Gather all patterns
with open('example.txt') as file:
    pattern = ""
    for line in file:
        pattern = line.strip()

new_string = ""
new_array = []

for i in range(len(pattern)):
    Rfirst = pattern[0 : len(pattern) - i] 
    Rsecond = pattern[len(pattern) - i : ] 
    new_string = Rsecond + Rfirst
    new_array.append(new_string)

final_string = ""

for l in sorted(new_array):
    final_string += l[-1:]

print(final_string)
    
