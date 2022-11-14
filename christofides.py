MST = kruskal(G)

M = min_match() 'na wierzchołkach nieparzystego stopnia'

'Multigraf= MST + M'

E = nx.eulerian_circuit(Multigraf)

'H = cykl Hamiltona z E'