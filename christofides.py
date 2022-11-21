from kruskal import *
from graph import *
from min_match import *
import networkx as nx

def christofides(G):
    MST = kruskal(G)

    degs = nx.degree(MST.to_nx())
    n = len(degs)
    MST_odd = list()

    for i in range(n):
        if degs[i][1]%2 != 0:
            MST_odd.append(degs[i][0])
        return MST_odd

    G_odd = nx.subgraph(G.to_nx(), MST_odd)
    M = min_match(G_odd)

    Multigraf = nx.union(MST,M)

    E = nx.eulerian_circuit(Multigraf)

    vertices = [u for u, v in nx.eulerian_circuit(E)]

    H = list()
    m = len(vertices)
    for i in range(m):
        if vertices[i] not in H:
            H.append(vertices[i])
        return(H)

    return(H)


