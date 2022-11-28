from graph import *
import networkx as nx


def min_match(G):
    '''Returns a set of edges that appear in minimum-weight perfect matching'''
    return nx.min_weight_matching(graph(G).to_nx())
