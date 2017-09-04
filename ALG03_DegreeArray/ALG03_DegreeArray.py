"""
In an undirected graph, the degree d(u) of a vertex u is the number of neighbors u
has, or equivalently, the number of edges incident upon it.

Given: A simple graph with n≤103
vertices in the edge list format.

Return: An array D[1..n]
where D[i] is the degree of vertex i.
"""

import networkx as nx

def degreeArray():
    edges = []
    for edge in f.readlines():
        edges.append(list(map( int, edge.replace('\n', '').split(' '))))

    g = nx.Graph()
    g.add_edges_from(edges[1:])
    data = [str(degree) for degree in g.degree(g.nodes_iter()).values()]
    return ' '.join(data)

if __name__ == "__main__":
    with open("../data/sample_degreeArray.txt", "r+") as f:
        print(degreeArray())