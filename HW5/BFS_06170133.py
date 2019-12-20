from collections import defaultdict 

class Graph:
    def __init__(self): 
        self.graph = defaultdict(list) 
 
    def addEdge(self,u,v): 
        self.graph[u].append(v)

    def BFS(self, s): 
        queue = []
        final = []
        final.append(s)
        queue = queue+self.graph[s]
        while len(queue) != 0:
            n = queue.pop(0)
            final.append(n)
            add = []
            add = add+self.graph[n]
            for i in add:
                if i in queue: #確認新加入的節點是不是已經在queue裡了，如果是，把add裡的移掉 
                    add.remove(i)
            queue = queue + add
            for i in final:
                if i in queue:#確定final裡的節點有沒有也在queue裡，有的話把queue裡的移掉
                    queue.remove(i)
        return final
    
    def DFS(self, s):
        stack = []
        final = []
        final.append(s)
        stack = stack+self.graph[s]
        while len(stack) != 0:
            n = stack.pop()
            final.append(n)
            add = []
            add = add+self.graph[n]
            for i in add:
                if i in stack:
                    add.remove(i)
            stack = stack + add
            for i in final:
                if i in stack:
                    stack.remove(i)
        return final
      
      
# 參考資料：
# http://www.csie.ntnu.edu.tw/~u91029/Graph.html
# http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
# https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
# https://github.com/tonyforreal/Tony-learning-note
# https://www.youtube.com/watch?v=bD8RT0ub--0&t=569s
