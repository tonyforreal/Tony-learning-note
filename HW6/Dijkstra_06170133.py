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
        import math

        values = [math.inf]*self.V
        values[s] = 0
        visited =  set()
        unvisited = set([x for x in range(self.V)])
        curr = s
        while curr is not None: 
            
            neighbors = self.graph[curr]
            for i, x in enumerate(neighbors):
                if x == 0 or i in visited: continue
                values[i] = min(values[i], values[curr] + x)

            visited.add(curr)
            unvisited.remove(curr)
            
            next_curr = None
            min_val = max(values)
            
            if not unvisited: break
            for node in unvisited:
                if values[node] < min_val:
                    next_curr = node
                    min_val = values[node]
            curr = next_curr
           
        ret = {str(i):x for i, x in enumerate(values)}
        return ret
    
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
