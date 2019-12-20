
# BFS原理：
### BFS又稱廣度優先搜尋法，是一種利用graph來搜索的演算法，從graph中的某個節點作為root開始走訪，接著走訪與root節點相鄰的所有節點，再由走訪過的節點用相同的觀念繼續搜索，也就是先找到所有廣度的節點後再往更深的節點搜索。若以tree來說，BFS必須先走訪完同一層的所有節點後才能繼續往下一層搜索，直到所有節點都被走訪到才停止。
### BFS是是利用Queue來處理，所以在pop走訪起始點的節點時永遠是pop出最早放進queue裡的節點，也就是最左邊的節點，所以是pop(0)。

# DFS原理：
### DFS又稱深度優先搜尋法，與BFS一億是利用graph來搜尋的演算法，也一樣是從graph中的某個節點開始走訪，與BFS不一樣的是，DFS並不像BFS要先將同一層的所有節點走訪過後才能往更深一層走，DFS則是起始節點走訪到相鄰的節點後，該相鄰的節點會變成新的起始節點，並繼續走訪相鄰的節點，換句話說DFS會優先往距離起始點最遠的地方走訪，若以tree來說，DFS會先不斷往更深一層的節點走訪，直到走到最深處後才回頭走訪Stack中的其他節點還有沒有相鄰節點，直到所有節點都被走訪到才停止。
### DFS是利用Stack來處理，由於Stack的特性，最早放進Stack的節點會在最底下的位子，而我們要丟出來的是Stack最上面的節點，所以是pop()。

# 流程圖：
## BFS：
![](/classnote/images/BFS.jpg)
## DFS：
![](/classnote/images/DFS.jpg)
# 學習歷程：
## Try 1：

### BFS的話依照原理的想法我寫出兩個空的list準備把pop出來的節點append進去，首先把起始點append進去，接著設一個while回圈確保如果queue裡還有東西就要繼續走訪，接著再設一個for回圈，如果其他節點沒有走訪過，也就是沒有在seen的list裡的話就把他append進去，最後回傳seen
### 而DFS則是把pop的方向改成最後面，以及把回圈反轉即可。


```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        queue = []
        seen = []
        queue.append(s)
        seen.append(s)
        while (len(queue) > 0) :
            v = queue.pop(0)
            nodes = self.graph[v]
            for i in nodes:
                if i not in seen:
                    queue.append(i)
                    seen.append(i)
        return seen

    def DFS(self, s):
        stack = []
        seen = []
        stack.append(s)
        seen.append(s)
        while (len(stack) > 0):
            v = stack.pop()
            nodes = self.graph[v]
            for i in reversed(nodes):
                if i not in seen:
                    stack.append(i)
                    seen.append(i)
        return seen


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print(g.BFS(2))
print(g.DFS(2))


```

    [2, 0, 3, 1]
    [2, 3, 0, 1]


### 以為成功了，但我換了更複雜的測值之後發現就錯了


```python
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self, s):
        queue = []
        seen = []
        queue.append(s)
        seen.append(s)
        while (len(queue) > 0):
            v = queue.pop(0)
            nodes = self.graph[v]
            for i in nodes:
                if i not in seen:
                    queue.append(i)
                    seen.append(i)
        return seen

    def DFS(self, s):
        stack = []
        seen = []
        stack.append(s)
        seen.append(s)
        while (len(stack) > 0):
            v = stack.pop()
            nodes = self.graph[v]
            for i in reversed(nodes):
                if i not in seen:
                    stack.append(i)
                    seen.append(i)
        return seen

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 0)
g.addEdge(2, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 2)
g.addEdge(4, 3)
g.addEdge(5, 3)
print(g.BFS(4))
print(g.DFS(4))
```

    [4, 2, 3, 0, 1, 5]
    [4, 3, 2, 0, 1, 5]


### BFS的部分沒錯但DFS很明顯錯了，4之後走訪到3，把3 pop出stack後填入的是1&5，故第三個走訪應該是5才對，看來上面的想法有錯，只好砍掉

## Try2：


### 這次就寫的嚴謹繁瑣一些，比較不同的是這次把queue與stack改成裝起始點的相鄰節點，final答案就直接先裝起始點進去了，while條件不改，接者不同的是在pop出下一個節點n後，把n的相鄰節點都裝進add裡面，然後利用for確定queue、stack裡面有沒有與add的節點重複，有的話把add裡的節點移除，最後兩個list加起來，就會把下一層的節點成功加進來了，接著再拿加好新節點的queue或stack與final比較有無重複節點，有的話把queue或stack的重複節點移除，然後繼續while回圈直到queue或stack裡都是空的，回傳final。


```python
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



g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 0)
g.addEdge(2, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.addEdge(3, 2)
g.addEdge(3, 4)
g.addEdge(3, 5)
g.addEdge(4, 2)
g.addEdge(4, 3)
g.addEdge(5, 3)
print(g.BFS(4))
print(g.DFS(4))
```

    [4, 2, 3, 0, 1, 5]
    [4, 3, 5, 1, 0, 2]


# 參考資料：
# http://www.csie.ntnu.edu.tw/~u91029/Graph.html
# http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
# https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
# https://github.com/tonyforreal/Tony-learning-note
# https://www.youtube.com/watch?v=bD8RT0ub--0&t=569s
