# Depth-First Search 
## 介紹
DFS屬於 recursive(遞迴) 的演算法。他主要的的想法就是先往某個方向走到底也就是 Depth-First 的意思，然後折返再去看他的分支，他會回朔，也就是走到底再往回找未被標記的節點，就像是 BST 的走訪。
![](https://i.imgur.com/Z6SIeJv.png)

### DFS VS. BFS 
![](https://i.imgur.com/gPqpwpO.png)

從兩者的步驟可以看到兩者概念很像，DFS就是很直接挑一邊的走到底再回頭找，使用Stack的結構。而 BFS 則是先以最接近的那一層開始，也就是他一走到某個節點時他就會把該點附近沒走過的節點都進入Queue。
- DFS: 以一邊優先
- BFS: 以階層關係優先
![](https://i.imgur.com/KDLXUCc.png)

### 課堂練習
![](https://i.imgur.com/jZSCB6o.png)

result: G->E->F->A->D->B->C
