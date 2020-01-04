# Stack & Queue
![](/classnote/img-for-readme/stack&queue.png)
## Stack的應用
* 網頁瀏覽器中回到上一頁功能。
* 任何遞迴(recursion)形式的演算法都可以用 Stack 改寫，例如 Depth-First Search(DFS,深度優先搜尋)

## Stack 必須有的功能
* **Push(Data)**: 把資料放到最上面(最新)。
* **Pop**: 把資料從最上面(最新)移除。
* **Top**: 回傳最上面(最新)的資料。
* **IsEmpty**: 確認stack 裡面是否有資料。
* **getSize**: 回傳stack 裡的資料個數。

## Queue的應用
* **應用在其他演算法**: 
    * Bread-First Search | 廣度優先搜尋
    * Tree 的 Level-Order Traversal | 二元樹走訪
* 作業系統被多個程式共享資源時(例如CPU、應表機、網站伺服器)，一次只能執行一個需求，所以需要用 Queue 來安排執行順序。

## Queue 必須有的功能
* **Push(Data)**: 把資料放到 Queue 的後面，並更新成新的 back。
* **Pop(dequeue)**: 把 front 所指向的資料從 Queue 中移除，並更新front。
* **getFront**: 回傳 front 所指向的資資料。
* **getBack**: 回傳 Back 所指向的資資料。
* **IsEmpty**: 確認 Queue 裡是否有資料。
* **getSize**: 確認 Queue 裡的資料個數。
