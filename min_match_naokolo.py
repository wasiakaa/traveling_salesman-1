import networkx as nx

def min_weight_matching(G, maxcardinality=None, weight="weight"):
    if maxcardinality not in (True, None):
        raise nx.NetworkXError(
            "The argument maxcardinality does not make sense "
            "in the context of minimum weight matchings."
            "It is deprecated and will be removed in v3.0."
        )
    if len(G.edges) == 0:
        return nx.max_weight_matching(G, maxcardinality=True, weight=weight)
    G_edges = G.edges(data=weight, default=1)
    max_weight = 1 + max(w for _, _, w in G_edges)
    InvG = nx.Graph()
    edges = ((u, v, max_weight - w) for u, v, w in G_edges)
    InvG.add_weighted_edges_from(edges, weight=weight)
    return nx.max_weight_matching(InvG, maxcardinality=True, weight=weight)



#G=nx.Graph()
#G.add_nodes_from([1,2, 3,4,5,6])
#G.add_weighted_edges_from([(1,3,3),(1,4,8),(1,5,5,),(2,3,1),(2,4,2),(4,6,4),(5,4,10),(5,6,1)])

#print(min_weight_matching(G))
