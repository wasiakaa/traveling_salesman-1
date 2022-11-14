class graph():
    def __init__(self, M):
        ''' M can be a dictionary or an adjacency matrix (list of lists) '''
        if(type(M)==dict):
            self.G= M
            return
        if(type(M)!=list):
            raise Exception("sorry, wrong type")
        #here i assume M is an adjacency matrix
        n = len(M)

        self.G = {}
        for i in range(n):
            self.G[i] = {}
            for j in range(n):
                if M[i][j]>0:
                    self.G[i][j]=M[i][j]
    def add_edge(self,a,b,w=1):
        '''a,b - vertices of a graph, add edge {a,b} with weight =w'''
        self.G[a][b]=w
        self.G[b][a] = w
    def to_nx(self):
        NXG=nx.empty_graph()
        for v in self.G:
            NXG.add_node(v)
        for v in self.G:
            for w in self.G[v]:
                NXG.add_edge(v,w,wegiht=self.G[v][w])
       
        return NXG
