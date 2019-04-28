import re
import operator
import numpy as np
import sys
sys.setrecursionlimit(3000000)

def construct_graph(array):
    graph = {}
    for line in array:
        edge = line.strip().split(' -> ')
        graph[edge[0]] = edge[1].split(',')

    return graph

def calc_degrees(graph):
    degrees = {}

    for node, neighbors in graph.items():
        degrees[node] = (0, len(neighbors))

    for _, neighbors in graph.items():
        for node in neighbors:
            if node in degrees:
                degrees[node] = (degrees[node][0] + 1, degrees[node][1])

    return degrees

def find_start_node(degrees):
    start_node = '0'

    for node, degree in degrees.items():
        if degree[0] < degree[1]:
            start_node = node

    return start_node

def find_eulerian_cycle(node, graph, cycle):
    cycle += [node]

    if len(graph[node]) == 0:
        return cycle

    while len(graph[node]) > 0:
        temp_node = graph[node][0]
        graph[node].remove(temp_node)

        sub_cycle = find_eulerian_cycle(temp_node, graph, [])

        cycle = cycle[:1] + sub_cycle + cycle[1:]

    return cycle

def find_eulerian_path(node, graph, degrees, path):
    path += [node]

    if node not in degrees or degrees[node][1] == 0:
        return path

    while len(graph[node]) > 0:
        temp_node = graph[node][0]
        graph[node].remove(temp_node)

        sub_path = find_eulerian_path(temp_node, graph, degrees, [])

        path = path[:1] + sub_path + path[1:]

    return path

with open("example.txt","r") as file:
    integers = file.readline().rstrip('\n');
    index = 0;
    dna_string = []

    #gather size of kmer and hammering distance
    for s in re.findall(r'\d+', integers):
        if index == 0:
            size_kmer = int(s);
        elif index == 1:
            num_kmers = int(s);
        index += 1

    motif = []
    temp_motif = []

    for dna in file:
        dna = dna.rstrip('\n').split('|');
        temp_motif.append(dna)

graph = {}

for kmer in temp_motif:
    for l in kmer:
        if l not in motif:
            motif.append(l)

for kmer in motif:
    prefix_ = kmer[:-1]
    suffix_ = kmer[1:]
    if prefix_ in graph.keys():
        graph[prefix_] += "," + suffix_
    else:
        graph[prefix_] = suffix_

#print(graph)

file_string = []

for l in graph:
    file_string.append(l + " -> " + graph[l])

graph = construct_graph(file_string)
degrees = calc_degrees(graph)
start_node = find_start_node(degrees)
#print(start_node)
eularian_path = find_eulerian_path(start_node, graph, degrees, [])
#print(eularian_path)
i = 0
final_string = ""
for kmer in eularian_path:
    if i == 0:
        final_string = kmer
    else:
        final_string += kmer[len(kmer)-1:]
    i += 1

print(final_string)
#print('->'.join(eularian_path))
