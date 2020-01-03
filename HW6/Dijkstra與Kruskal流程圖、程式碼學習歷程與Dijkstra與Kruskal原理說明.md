
# Dijkstra:
### 又稱最短路徑，利用BFS的圖來說，就是在連接點與點之間的邊上加上距離，計算從起點(s)出發到各點的最短距離是多少，並產生一個最短路徑樹。
### Dijkstra的時間複雜度為O(N²)

# Kruskal:
### Kruskal（MST）是利用貪婪演算法(greedy algorithm)的思維，也就是每一步都要採取最佳的選擇，進而讓結果也會是最佳的演算法。Kruskal要在graph裡尋找出走訪所有點後的最小權重和，換句話說就是在從出發點開始，經過所有點，到達最後一個點所走的長度要是最短的。
### Kruskal的時間複雜度為O(NlogN)

# 流程圖：
## Dijkstra:
![](/classnote/images/dijkstra.jpg)

## Kruskal:
![](/classnote/images/kruskal.jpg)


# 學習歷程：
## Dijkstra:
### 一開始先設兩個list，第一個list先設點到點的距離都是無限大為distance，另一個設都是False，為了檢測各點是否已經被走過了，如果走過了就改成True。 迴圈設while test != [True] * self.V，也就是如果還有還沒走完的點就繼續跑，再來假如是從0開始，0到0的距離就是0，也就是說當條件一:g.graph不等於0，和條件二:distance[現在點的index] + g.graph小於原來的distance[0-self.V的index]，兩個條件都達成的時候，distance[0-self.V的index]會等於distance[現在點的index] + g.graph，因為路徑更短。
### 接著找完剩下還沒被走過的點中，距離最小的那個點和那個點的index，最後再把False改成True





```python
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
        answer = {} 
        
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
            
            
            if test == [True] * self.V:
                for i in range(self.V):
                    answer[str(i)] = distance[i]
                return answer
            
            
            
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],
          [0,0,2,0,0,0,6,7,0]]

print('Dijkstra',g.Dijkstra(0))
```

    Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}


## Kruskal:
### 一樣先設一個空的dict裝答案，把self.v都裝進check裡面
### 設一個變數為從小到大排序過的權重叫val，接著開始寫巢狀迴圈，第一層先設權重為i，第二層設f,s是第一個點與第二個點，如果兩邊check都一樣就pass不做任何動作，else是把s的起始點全都轉f的起始點，最後把answer的格式設定成助教規定的“點-點：權重”後就可以了。


```python
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
    
g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
print('Kruskal',g.Kruskal())
```

    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}



```python
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
    
    
    
g = Graph(9)
g.graph = [[0,4,0,0,0,0,0,8,0],
          [4,0,8,0,0,0,0,11,0],
          [0,8,0,7,0,4,0,0,2],
          [0,0,7,0,9,14,0,0,0],
          [0,0,0,9,0,10,0,0,0],
          [0,0,4,14,10,0,2,0,0],
          [0,0,0,0,0,2,0,1,6],
          [8,11,0,0,0,0,1,0,7],
          [0,0,2,0,0,0,6,7,0]]

print('Dijkstra',g.Dijkstra(0))

g = Graph(4)
g.addEdge(0,1,10)
g.addEdge(0,2,6)
g.addEdge(0,3,5)
g.addEdge(1,3,15)
g.addEdge(2,3,4)
print('Kruskal',g.Kruskal())
```

    Dijkstra {'0': 0, '1': 4, '2': 12, '3': 19, '4': 21, '5': 11, '6': 9, '7': 8, '8': 14}
    Kruskal {'2-3': 4, '0-3': 5, '0-1': 10}


# 參考資料：
# https://www.youtube.com/watch?v=9wV1VxlfBlI
# https://github.com/tonyforreal/Tony-learning-note
# http://blog.yslin.tw/2012/05/python-listdict.html sorted()用法
# https://sites.google.com/site/ezpythoncolorcourse/nestedforloop 巢狀迴圈
# https://github.com/yunghsin615/little_sun


```python

```
