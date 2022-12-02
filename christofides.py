from kruskal import *
import graph
from min_match import *
import networkx as nx


def odd_deg_vertices(G):
    '''Returns a list of odd-degree vertices of G'''

    degs = list(nx.degree(G.to_nx()))
    n = len(degs)
    G_odd = list()

    for j in range(n):
        if degs[j][1] % 2 != 0:
            G_odd.append(degs[j][0])

    return G_odd


def multigraph(G, H):
    '''Returns a multigraph made from edges of graphs G and H'''
    multi_G = nx.MultiGraph()
    multi_G.add_edges_from(G.edges())

    multi_H = nx.MultiGraph()
    multi_H.add_edges_from(H.edges())

    multi_G.update(edges=multi_H.edges())

    return multi_G


def ham_from_eul(E):
    '''Returns vertices of a Hamiltonian cycle made from
    consecutive varying vertices of an Eulerian cycle E'''

    vertices = [u for u, v in E]
    H = list()
    m = len(vertices)

    for j in range(m):
        if vertices[j] not in H:
            H.append(vertices[j])

    return H


def christofides(G):
    '''Returns vertices of a Hamiltonian cycle with the cost lower or equal
     to 1.5 of the cost of the optimal Hamiltonian cycle in graph G'''

    # minimum spanning tree
    MST = graph(kruskal(G))
    # odd-degree vertices of MST
    MST_odd = odd_deg_vertices(MST)

    # subgraph of G induced by odd-degree vertices of MST
    G_odd = nx.subgraph(G.to_nx(), MST_odd)
    # minimum-weight perfect matching of G_odd
    M = nx.Graph()
    M.add_edges_from(nx.min_weight_matching(G_odd))

    # multigraph made from edges of MST and M
    multi = multigraph(MST.to_nx(), M)

    # Eulerian cycle in multigraph (starting in '0' vertex)
    E = nx.eulerian_circuit(multi, source='0')

    # Hamiltonian cycle made from consecutive varying vertices of E
    H = ham_from_eul(E)

    return H


# example

# G3 = graph({'0': {'1': 1, '2': 2, '3': 2, '4': 4}, '1': {'0': 1, '2': 2, '3': 5, '4': 6},
#             '2': {'0': 2, '1': 2, '3': 2, '4': 2}, '3': {'0': 2, '1': 5, '2': 2, '4': 1},
#             '4': {'0': 4, '1': 6, '2': 2, '3': 1}})
#
# print(christofides(G3))
