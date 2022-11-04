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



M=[[0,0,1],[3,0,1],[4,5,0]]
grafus=graph(M)
#print(grafus.G)
grafus2=graph(grafus.G.copy())
grafus.add_edge(0,1,100)

#(grafus.G)
dicto={

    "a": {"b":2,"c":2},
    "b": {"b":20},
    "c": {"a":177},
    "d": {}
}


#print(grafus.G[1].keys())
#print(list(dicto["a"]))
#print(len(dicto)) #O(1)
#print(dicto["d"]=={})
#print(min(dicto["a"],key=dicto["a"].get))


del dicto["a"]["b"]
print(dicto)