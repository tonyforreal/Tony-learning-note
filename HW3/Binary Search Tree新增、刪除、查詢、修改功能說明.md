# 功能說明:
## 1.新增:
### 首先確認BST中有沒有root，沒有的話新增的值就直接變成這棵BST的root。
### 若這棵BST已經有root了，那新增節點的第一步是確認填入的值是大於還是小於root，小於的話往root的左子節點走，大於往root的右子節點走，若子節點有node則重複上述步驟，利用不斷與parent比較的方法往下走找到一個空位的子節點，填入新值。
### 以下圖為例，現在有一顆root為20，leftchild為10，rightchild為30的BST。
![](/classnote/images/insert1.png)
### 我要新增15進這棵樹，第一步確認15是大於還是小於root的20，是小於所以往左走，但root的左邊已經有小孩了所以繼續跟左邊小孩比較，15比10大所以15往右走，而10沒有任何子節點所以15就會新增在10的右下方。
![](/classnote/images/insert2.png)


## 2.刪除:
### 刪除會碰到的狀況有三種：
* 1.要刪除的節點沒有任何子節點
* 2.要刪除的節點有一個子節點
* 3.要刪除的節點有兩個子節點
### 1.這是最理想的狀況，只需要把該節點刪除即可。
### 2.刪除該節點後，需把該節點的子節點接到該節點的父節點上。
#### 圖示：
![](/classnote/images/delete1.png)
### 3.刪除該節點後，要找到該節點的 **左子樹中的最大值** 取代該節點的位置即可。
#### 圖示：
![](/classnote/images/delete2.png)


## 3.查詢:
### 查詢的原理與[新增](#1新增)相似，假設我們要查詢的Node為target，首先一樣先確認root是不是空的，如果是表示這棵樹也是空的所以查詢結果為None。
### 若有root存在，開始用target與root比大小，target較小的話往root的左子節點走，target較大則往root的右子節點走。與新增不一樣的地方是，查詢停止往下比較的條件一種是樹中沒有target對應的Node，一種是樹中有target對應的Node。
### 我們就以剛剛[新增](#1新增)使用的BST舉例:
![](/classnote/images/insert2.png)
### ex1:假設我要查詢的值為15，第一步先與root比大小，15<20所以往左下走，碰到10所以繼續比大小，15>10所以往右下走，碰到15發現15==15，就完成查詢了。
### ex2:假設我要查詢的值為18，第一步先與root比大小，18<20所以往左下走，碰到10所以繼續比大小，18>10所以往右下走，碰到15所以繼續比大小，18>15所以往右下走，發現沒有其他節點了，所以回傳None。




## 4.修改:
### 一樣利用[查詢](#3查詢)來找到要修正的target，然後利用刪除跟新增來將新修改的Node加進來，取代原本的Node。

# 參考資料：
## https://medium.com/@Kadai/%E8%B3%87%E6%96%99%E7%B5%90%E6%A7%8B%E5%A4%A7%E4%BE%BF%E7%95%B6-binary-search-tree-3c40be3204e
## https://github.com/tonyforreal/Tony-learning-note/blob/master/HW3/BST%E5%8A%9F%E8%83%BD%E8%AA%AA%E6%98%8E.md
## http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html
