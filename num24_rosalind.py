import sys

def construct_graph(file_path):
    with open(file_path) as fh:
        graph = {}
        for line in fh:
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

if __name__ == '__main__':
    graph = construct_graph(sys.argv[1])
    print(graph)
    degrees = calc_degrees(graph)
    start_node = find_start_node(degrees)
    eularian_path = find_eulerian_path(start_node, graph, degrees, [])
    print('->'.join(eularian_path))
