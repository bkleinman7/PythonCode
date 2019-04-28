def read_file(input_file):

    f = open(input_file)
    raw_input = f.readlines()
    f.close()

    return raw_input


class Trie:
    
    def __init__(self):
        self.counter = count(start=1)
        self.root = [next(self.counter),{}]

    def insert(self, sequence):
        node = self.root
        for ch in sequence:
            if ch not in node[1]:
                node[1][ch] = [next(self.counter),{}]
            node = node[1][ch]


def trie(sequences):
    myTrie = Trie()
    for sequence in sequences:
        myTrie.insert(sequence)
    return myTrie.root


result = []
def Format(node):
    for ch, node2 in node[1].iteritems():
        result.append(str(node[0]-1) + '->' + str(node2[0]-1) + ':' + str(ch))
        Format(node2)
    return result


if __name__ == '__main__':

    import sys
    import doctest
    from itertools import count

    raw_data = read_file(sys.argv[-1])
    seqs = [item.strip() for item in raw_data]
    fw = open('./output.txt','w')
    for item in Format(trie(seqs)):
        fw.write(item + '\n')
    fw.close()
