'''
Double-Degree Array
Given: A simple graph with n≤10^3 vertices in the edge list format.
Return: An array D[1..n] where D[i] is the sum of the degrees of i's neighbors.
'''

def ddeg_array(num_vertices, edges):
    # adjacency dictionary with vertices as keys,
    # lists of adjacent vertices as values
    adj = {k:[] for k in range(1,num_vertices + 1)}
    for v1, v2 in edges:
       adj[v1].append(v2)
       adj[v2].append(v1)

    # degree of a vertex is the number of edges that connect to it
    # double degree of a vertex is the number of edges that are connected to adjacent vertices

    ddeg = {k:0 for k in adj.keys()}
    ans = []
    for vert in adj:
        for n in adj[vert]:
            ddeg[vert] += len(adj[n])

    for k, v in sorted(ddeg.items()):
        ans.append(v)
    return ans


if __name__ == '__main__':
    infile = 'rosalind_ddeg.txt'
    with open(infile) as data:
        # read data in edgelist format:
        # 1st line: number of vertices, number of edges
        # subsequent lines: edge given by two vertices
        num_vertices, num_edges = map(int, data.readline().rstrip().split())
        edges = [map(int, line.rstrip().split()) for line in data]

    print(*ddeg_array(num_vertices,edges) )

