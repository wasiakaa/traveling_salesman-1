from graph import *
import networkx as nx
def min_match(Graf):
    return nx.min_weight_matching(Graf.to_nx())


