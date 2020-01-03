from collections import defaultdict 


class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.dict = defaultdict(list) 
    
    def addEdge(self,u,v,w): 
        self.dict[w].append([u,v])
    
    def Dijkstra(self, s): 
        test = [False] * self.V 
        distance = [float('inf')] * self.V
        
        distance[s] = 0
        
        while test != [True] * self.V:
            for i in range(self.V):
                if g.graph[s][i] != 0 and distance[s] + g.graph[s][i] < distance[i]:
                    distance[i] = distance[s] + g.graph[s][i]
                           
            m = float('inf')
            for k in range(self.V):
                if test[k] == False and distance[k] < m :
                    m = distance[k]
                    s = k         
            test[s] = True
            
            answer = {} 
            if test == [True] * self.V:
                for i in range(self.V):
                    answer[str(i)] = distance[i]
                return answer
    
    def Kruskal(self):
        answer={}
        check = []
        for i in range(self.V):
            check.append(i)
        val = sorted(self.dict)
        for i in val:
            for f,s in self.dict[i]:
                if check[f] == check[s]:
                    pass
                else:
                    check = [check[f] if x==check[s] else x for x in check]
                    answer[str(f)+'-'+str(s)] = i
        return answer
