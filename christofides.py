from kruskal import *
import graph
from min_match import *
import networkx as nx


def christofides(G):
    '''Returns vertices of a Hamiltonian cycle with the cost lower or equal
     to 1.5 of the cost of the optimal Hamiltonian cycle in graph G.'''

    # minimum spanning tree
    MST = graph(kruskal(G))

    # odd-degree vertices of MST
    degs = list(nx.degree(MST.to_nx()))
    n = len(degs)
    MST_odd = list()

    for j in range(n):
        if degs[j][1] % 2 != 0:
            MST_odd.append(degs[j][0])

    # subgraph of G induced by odd-degree vertices of MST
    G_odd = nx.subgraph(G.to_nx(), MST_odd)
    # minimum-weight perfect matching of G_odd
    M = nx.Graph()
    M.add_edges_from(min_match(G_odd))

    # multigraph made from edges of MST and M
    multi_MST = nx.MultiGraph()
    multi_MST.add_edges_from(nx.edges(MST.to_nx()))

    multi_M = nx.MultiGraph()
    multi_M.add_edges_from(M.edges())

    multi_MST.update(edges=multi_M.edges())
    multigraph = multi_MST

    # Eulerian cycle in multigraph (starting in '0' vertex)
    E = nx.eulerian_circuit(multigraph, source='0')

    # hamiltonian cycle made from consecutive varying vertices of E
    vertices = [u for u, v in E]
    H = list()
    m = len(vertices)
    for j in range(m):
        if vertices[j] not in H:
            H.append(vertices[j])

    return H


# example

# G3 = graph({'0': {'1': 1, '2': 2, '3': 2, '4': 4}, '1': {'0': 1, '2': 2, '3': 5, '4': 6},
            # '2': {'0': 2, '1': 2, '3': 2, '4': 2}, '3': {'0': 2, '1': 5, '2': 2, '4': 1},
            # '4': {'0': 4, '1': 6, '2': 2, '3': 1}})

# print(christofides(G3))
