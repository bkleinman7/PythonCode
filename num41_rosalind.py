patterns = []

#Gather all patterns
with open('example.txt') as file:
    for line in file:
        patterns.append(line.strip())

new_patterns = []

for i in range(len(patterns[0])):
    size = len(patterns[0])
    string = patterns[0]
    new_patterns.append(string[i:])

new_map = {}

for i in range(len(new_patterns)):
    new_map[new_patterns[i]] = i

new_string = ""

for i in sorted(new_patterns):
    new_string += str(new_map[i]) + ', '

text_file = open("Output.txt", "w")
text_file.write(new_string)
text_file.close()
