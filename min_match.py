from graph import *
import networkx as nx


def min_match(Graf):
    return nx.min_weight_matching(graph(Graf).to_nx())
