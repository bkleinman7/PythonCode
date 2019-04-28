patterns = []

def trieconstruction(Patterns):
    Trie_edge = {}
    Trie = {}
    pattern_max = 0
    new_string = ""
    suffix_array = []
    for pattern in patterns:
        branch_path = False
        #print(new_string)
        for i in range(len(pattern)):
            key = str(i) + pattern[0]
            if branch_path == True:
                pattern_max += 1
                if key not in Trie_edge.keys():
                    Trie_edge[key] = pattern[i]
                else:
                    Trie_edge[key] = Trie_edge[key] + pattern[i]
                Trie[str(pattern_max-1) + '->' + str(pattern_max)] = pattern[i]
                new_string += pattern[i]
                continue
            
            new_string = ""
            if key not in Trie_edge.keys():
                new_string += pattern[i]
                Trie_edge[key] = pattern[i]
                Trie[str(i) + '->' + str(pattern_max+1)] = pattern[i]
                pattern_max += 1
                branch_path = True
            else:
                if pattern[i] in Trie_edge[key]:
                    continue
                else:
                    pattern_max += 1
                    Trie_edge[key] = Trie_edge[key] + pattern[i]
                    Trie[str(i) + '->' + str(pattern_max)] = pattern[i]
                    new_string += pattern[i]
                    branch_path = True
        print(new_string)
    #print(suffix_array)
    return(Trie)
    
#Gather all patterns
with open('example.txt') as file:
    for line in file:
        patterns.append(line.strip())

Trie = trieconstruction(patterns)
#print(Trie)
#output to file...
text_file = open("Output.txt", "w")
for k, v in Trie.items():
    text_file.write(k + ':' + v + '\n')
    #print(k + ':' + v)
text_file.close()
