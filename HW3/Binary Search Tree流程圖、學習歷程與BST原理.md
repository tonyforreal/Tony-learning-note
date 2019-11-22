
# Binary Search Tree
## BST是什麼？
### Binary search tree是個二元樹的結構，每個節點最多只會有兩個小孩，一左一右。而排序規則則是**比parent小的node擺左邊，比parent大的node擺右邊**，而這個原理也是insert、search跟delete所使用的找點方式，以search為例，若我要找的target比parent還大就往parent.right的位子繼續往下找，比parent小則往parent.left找，直到節點與target相等就結束search。

### 而時間複雜度則是看二元樹的高度決定，最佳情況為O(1)，平均情況與最差情況為O(log n)。

# 流程圖：
# insert:
![](/classnote/images/insert.jpg)
# delete:
![](/classnote/images/delete.jpg)
# search:
![](/classnote/images/search.jpg)
# modify:
![](/classnote/images/modify.jpg)

# 學習歷程：
## insert:
### 這是我第一次打insert的程式碼，因為想與其他人比較不同的關係，所以我設了兩個def，insert的原理是要判斷植入的值是否符合BST的規則，也就是左小右大。insert的第一步要確定root是不是空的，也就是這棵樹是不是空的，是的話，第一個填入的值就會是這棵樹的root。


```python
def insert(self, root, val):
        if root==None:
            root=TreeNode(val)
        else:
            self.insert_again(val, root)
        return TreeNode(val)
            

```

### 如果不幸root已經有node了，那就得跑第二個function。假設我們要植入的值叫做val，而insert_again會碰到的狀況是：已經有root了，如果val比root小，那val就得往root.left走，而往左走又會遇到兩種狀況：1.如果root.left是空的，那val就可以直接變成root的leftchild。2.如果root.left有node了，則利用遞迴再跑一次insert_again的函式，而帶入該函式的值變成(val, root.left)再跑一次直到val找到空的子節點才結束，若val比root大則往root.right走，後面則與往左走類似，只差在往左下與往右下尋找空的子節點。



```python
def insert_again(self, val, current):
    if val<=current.val: #目前的current.val是root.val
        if current.left is None: #如果root左下沒有數則把帶入的數變成左邊的小孩
            current.left=TreeNode(val)
        else:
            self.insert_again(val, current.left) #如果有的話則再跑一次insert_again讓他判斷val比左邊小孩大還小
    else:
        if current.right is None:
            current.right=TreeNode(val)
        else:
            self.insert_again(val, current.right)
```

## 結果如下：


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def insert(self, root, val):
        if root==None:
            root=TreeNode(val)
        else:
            self.insert_again(val, root)
        return TreeNode(val)
            
    def insert_again(self, val, current):
        if val<=current.val: #目前的current.val是self.root
            if current.left is None: #如果root左下沒有數則把帶入的數變成左邊的小孩
                current.left=TreeNode(val)
            else:
                self.insert_again(val, current.left) #如果有的話則再跑一次insert_again讓他判斷val比左邊小孩大還小
        else:
            if current.right is None:
                current.right=TreeNode(val)
            else:
                self.insert_again(val, current.right)
                
                
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print("insert")
print(Solution().insert(root1, 4) == root1.left.right)
print("------------------------------------------")
print(Solution().insert(root1, 4).val)
print(root1.left.right.val)
```

    insert
    False
    ------------------------------------------
    4
    4


### 這裡我比較疑惑的是我兩邊的val皆為4了，但兩邊比較時卻是False，於是我用print兩邊的.val去掉檢查，得到下面結果：


```python
print(Solution().insert(root1, 4))
print(root1.left.right)
```

    <__main__.TreeNode object at 0x10a48e7b8>
    <__main__.TreeNode object at 0x10a4aecc0>


### 我發現兩點所儲存的位址不一樣，所以我又回到原本的程式碼檢查

### 花了大概2個小時思索與嘗試後我發現我的遞迴與return有衝突，我在insert_again後不應該return TreeNode(val)，而是應該直接return insert_again後的結果。於是改正後總算可以跑出True。


```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def insert(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root
        else:
            return self.insert_again(val, root)

    def insert_again(self, val, current):
        if val <= current.val:  # 目前的current.val是root.val
            if current.left is None:  # 如果root左下沒有數則把帶入的數變成左邊的小孩
                current.left = TreeNode(val)
                return current.left
            else:
                return self.insert_again(val, current.left)  # 如果有的話則再跑一次insert_again讓他判斷val比左邊小孩大還小
        else:
            if current.right is None:
                current.right = TreeNode(val)
                return current.right
            else:
                return self.insert_again(val, current.right)
            
            
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print("insert")
print(Solution().insert(root1, 4) == root1.left.right)
print("------------------------------------------")

```

    insert
    True
    ------------------------------------------


## search:

### search是我認為四個函式中最好寫的一個，觀念與insert類似，一樣利用BST左小右大的原理，利用遞迴去不斷往下找直到target等於節點的值後停止。
### 第一次測試我寫出四個條件分別是：1.target等於root  2.target大於root   3.target小於root  4.樹中沒有與target相符的值


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def search(self, root, target):
        if root.val==target:
            return root
        elif root.val<target:
            self.search(root.right, target)
        elif root.val>target:
            self.search(root.left, target)
        else:
            return None

        
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# search
print("search")
print(Solution().search(root2, 10) == root2.right.right)
print(Solution().search(root2, 10))
print(root2.right.right)
```

    search
    False
    None
    <__main__.TreeNode object at 0x10a52ab00>


### 好又False了，看到結果跑出None我就馬上懷疑我一定是少return東西出來，於是回去看程式碼後，我原本的想法是利用遞迴讓兩個elif裡的(root.left,root.right)利用return root回傳出來，但想了想後覺得這想法蠻蠢的，return root就只會return root出來，所以補齊兩個return後結果如下：


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def search(self, root, target):
        if root.val == target:
            return root
        elif root.val < target:
            return self.search(root.right, target)
        elif root.val > target:
            return self.search(root.left, target)
        else:
            return None
        
        
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
print("search")
print(Solution().search(root2, 10) == root2.right.right)
print(Solution().search(root2, 10))
print(root2.right.right)
```

## delete:

### 我在delete的時候我想利用上面的search函式來尋找要刪除的target，但我發現我的search打法會導致後面出現error


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def search(self, root, target):
        if root.val == target:
            return root
        elif root.val < target:
            return self.search(root.right, target)
        elif root.val > target:
            return self.search(root.left, target)
        else:
            return None
        
    def findleftnode(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def delete(self, root, target):
        while self.search(root, target) is not None:
            if root is None:
                return root
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif target > root.val:
                root.right = self.delete(root.right, target)
            else:
                if root.right is None and root.left is not None:
                    x = root.left
                    root = None
                    return x
                elif root.left is None and root.right is not None:
                    x = root.right
                    root = None
                    return x

                x = self.findleftnode(root.right)
                root.val = x.val
                root.right = self.delete(root.right, x.val)
        return root
    
    
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
print("delete")
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)

```

    delete



    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-2-a97925c4f251> in <module>
         66 root4 = copy.deepcopy(root)
         67 print("delete")
    ---> 68 root2 = Solution().delete(root2,3)
         69 print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
         70 print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)


    <ipython-input-2-a97925c4f251> in delete(self, root, target)
         22 
         23     def delete(self, root, target):
    ---> 24         while self.search(root, target) is not None:
         25             if root is None:
         26                 return root


    <ipython-input-2-a97925c4f251> in search(self, root, target)
         12             return self.search(root.right, target)
         13         elif root.val > target:
    ---> 14             return self.search(root.left, target)
         15         else:
         16             return None


    <ipython-input-2-a97925c4f251> in search(self, root, target)
         10             return root
         11         elif root.val < target:
    ---> 12             return self.search(root.right, target)
         13         elif root.val > target:
         14             return self.search(root.left, target)


    <ipython-input-2-a97925c4f251> in search(self, root, target)
          7 class Solution(object):
          8     def search(self, root, target):
    ----> 9         if root.val == target:
         10             return root
         11         elif root.val < target:


    AttributeError: 'NoneType' object has no attribute 'val'


### 所以我決定再寫一個專門給delete使用的search，我命名為find_target，因為原本的search是錯在root.val == target:，所以我改寫了一下。


```python
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def search(self, root, target):
        if root.val == target:
            return root
        elif root.val < target:
            return self.search(root.right, target)
        elif root.val > target:
            return self.search(root.left, target)
        else:
            return None
    
    def findleftnode(self, node):
        while node.left is not None:
            node = node.left
        return node

    def find_target(self, root, target):
        if root is None:
            return None
        else:
            if root.val == target:
                return root
            elif root.val < target:
                return self.find_target(root.right, target)
            else:
                return self.find_target(root.left, target)

    def delete(self, root, target):
        while self.find_target(root, target) is not None:
            if root is None:
                return root
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif target > root.val:
                root.right = self.delete(root.right, target)
            else:
                if root.right is None and root.left is not None:
                    x = root.left
                    root = None
                    return x
                elif root.left is None and root.right is not None:
                    x = root.right
                    root = None
                    return x

                x = self.findleftnode(root.right)
                root.val = x.val
                root.right = self.delete(root.right, x.val)
        return root
    
    
    
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
print("delete")
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
```

    delete
    True
    True
    True
    True


### 但我又發現可能的bug，因為我的findleftnode只找了最左邊的值來跟root對換，若遇到只有左邊有子節點的樹，會沒辦法換root的值做刪除，所以我詢問盧煒中同學怎麼解決，最後我依照他教的觀念再打一次delete，結果如下：


```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
         self.sear = None
         self.node = None
         self.target = None
    def switch(self,root):
        if root.right is None and root.left is None: #如果兩邊都沒有小孩就return None
            return None
        elif root.right is not None and root.left is not None: #如果兩邊都有小孩則跟只有左邊有小孩的作法相同
            x = root.left 
            while x.right is not None: 
                x = x.right 
            root.val = x.val 
            root.left = self.delete(root.left,root.val) 
            return root
        elif root.right is not None and root.left is None: #如果右邊有小孩就跟下面差不多了只差在往左下或右下找最下面的節點替換後刪掉
            x = root.right 
            while x.left is not None:
                x = x.left
            root.val = x.val
            root.right = self.delete(root.right,root.val)
            return root
        elif root.right is None and root.left is not None:#如果左邊有小孩
            x = root.left#把root的左小孩佔存在x
            while x.right is not None:#如果x.right有Node就繼續找
                x = x.right#直到最下面的右節點被找到
            root.val = x.val#把要刪的root值換成最右下的節點的值
            root.left = self.delete(root.left,root.val)#換完後把右下的節點刪掉
            return root
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if self.target is None: 
            self.target = target
        if target < root.val: #如果要刪的值比root.val小
            if root.left is None: #如果root沒有左小孩則直接回傳None
                return None
            else: #如果有左小孩
                root.left = self.delete(root.left, target) #用root.left回到delete再跑一次
                return root
        elif target > root.val: #如果要刪的值大於root.val
            if root.right is None: #如果root沒有右小孩則回傳None
                return None
            else: #如果有
                root.right = self.delete(root.right, target) #用root.right回到delete再跑一次
                return root
        elif root.val == target: #所以最後如果樹中有要刪的值會跑到這行
            root = self.switch(root) #把target帶去switch函式跑
            if root is not None and root.val == self.target:
                root = self.switch(root)
            return root
        
        
import copy
root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
print("delete")
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
```

    delete
    True
    True
    True
    True


## modify:
### 最後的modify我打算用到前面寫出來的三個函式來寫，先用search去找target在哪，接著用delete把target刪掉，最後用insert把修改的值填進來，結果如下：


```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
         self.sear = None
         self.node = None
         self.target = None

    def insert(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root
        else:
            return self.insert_again(val, root)

    def insert_again(self, val, current):
        if val <= current.val:  # 目前的current.val是self.root
            if current.left is None:  # 如果root左下沒有數則把帶入的數變成左邊的小孩
                current.left = TreeNode(val)
                return current.left
            else:
                return self.insert_again(val, current.left)  # 如果有的話則再跑一次insert_again讓他判斷val比左邊小孩大還小
        else:
            if current.right is None:
                current.right = TreeNode(val)
                return current.right
            else:
                return self.insert_again(val, current.right)

    def search(self, root, target):
        if root.val == target:
            return root
        elif root.val < target:
            return self.search(root.right, target)
        elif root.val > target:
            return self.search(root.left, target)
        else:
            return None

    def switch(self,root):
        if root.right is None and root.left is None:
            return None
        elif root.right is not None and root.left is not None:
            x = root.left
            while x.right is not None:
                x = x.right
            root.val = x.val
            root.left = self.delete(root.left,root.val)
            return root
        elif root.right is not None and root.left is None:
            x = root.right
            while x.left is not None:
                x = x.left
            root.val = x.val
            root.right = self.delete(root.right,root.val)
            return root
        elif root.right is None and root.left is not None:
            x = root.left
            while x.right is not None:
                x = x.right
            root.val = x.val
            root.left = self.delete(root.left,root.val)
            return root
        
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if self.target is None:
            self.target = target
        if target < root.val:
            if root.left is None:
                return None
            else:
                root.left = self.delete(root.left, target)
                return root
        elif target > root.val:
            if root.right is None:
                return None
            else:
                root.right = self.delete(root.right, target)
                return root
        elif root.val == target:
            root = self.switch(root)
            if root is not None and root.val == self.target:
                root = self.switch(root)
            return root
        
    def modify(self, root, target, new_val):
        x = 0 #隨便設一個變數，等等新增會用到
        y = self.search(root,target) #用search去尋找target的位子，暫存在y
        if y is not None and y.val == target: 
            x = x + 1 #每當target等於y的值，x就加1一次
            y = y.left #y往左走
        self.delete(root,target) #把target都刪除
        
        for i in range(x): 
            self.insert(root,new_val)#新增修改的值進來
        return root
            
            
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
root = Solution().modify(root,7,4)
print(root.right.left.val)
print(root.left.right.val)
```

    6
    4


## 最後測試：


```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
         self.sear = None
         self.node = None
         self.target = None

    def insert(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root
        else:
            return self.insert_again(val, root)

    def insert_again(self, val, current):
        if val <= current.val:  # 目前的current.val是self.root
            if current.left is None:  # 如果root左下沒有數則把帶入的數變成左邊的小孩
                current.left = TreeNode(val)
                return current.left
            else:
                return self.insert_again(val, current.left)  # 如果有的話則再跑一次insert_again讓他判斷val比左邊小孩大還小
        else:
            if current.right is None:
                current.right = TreeNode(val)
                return current.right
            else:
                return self.insert_again(val, current.right)

    def search(self, root, target):
        if root.val == target:
            return root
        elif root.val < target:
            return self.search(root.right, target)
        elif root.val > target:
            return self.search(root.left, target)
        else:
            return None

    def switch(self,root):
        if root.right is None and root.left is None:
            return None
        elif root.right is not None and root.left is not None:
            x = root.left
            while x.right is not None:
                x = x.right
            root.val = x.val
            root.left = self.delete(root.left,root.val)
            return root
        elif root.right is not None and root.left is None:
            x = root.right
            while x.left is not None:
                x = x.left
            root.val = x.val
            root.right = self.delete(root.right,root.val)
            return root
        elif root.right is None and root.left is not None:
            x = root.left
            while x.right is not None:
                x = x.right
            root.val = x.val
            root.left = self.delete(root.left,root.val)
            return root
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: None Do not return anything, delete nodes(maybe more than more) instead.(cannot search())
        """
        if self.target is None:
            self.target = target
        if target < root.val:
            if root.left is None:
                return None
            else:
                root.left = self.delete(root.left, target)
                return root
        elif target > root.val:
            if root.right is None:
                return None
            else:
                root.right = self.delete(root.right, target)
                return root
        elif root.val == target:
            root = self.switch(root)
            if root is not None and root.val == self.target:
                root = self.switch(root)
            return root
        
    def modify(self, root, target, new_val):
        x = 0 
        y = self.search(root,target) 
        if y is not None and y.val == target: 
            x = x + 1 
            y = y.left 
        self.delete(root,target) 
        
        for i in range(x): 
            self.insert(root,new_val)
        return root
    
    

import copy

root = TreeNode(5)
Node1 = TreeNode(3)
Node2 = TreeNode(3)
Node3 = TreeNode(-5)
Node4 = TreeNode(8)
Node5 = TreeNode(7)
Node6 = TreeNode(6)
Node7 = TreeNode(10)
root.left = Node1
root.right = Node4
Node1.left = Node2
Node2.left = Node3
Node4.left = Node5
Node5.left = Node6
Node4.right = Node7
root1 = copy.deepcopy(root)
root2 = copy.deepcopy(root)
root3 = copy.deepcopy(root)
root4 = copy.deepcopy(root)
# insert
print("insert")
print(Solution().insert(root1, 4) == root1.left.right)
print("------------------------------------------")
# delete
print("delete")
root2 = Solution().delete(root2,3)
print(root2.val == 5 and root2.left.val == -5 and root2.left.left == None and root2.left.right == None)
print(root2.right.right.val == 10 and root2.right.left.val == 7 and root2.right.left.left.val == 6)
print(root2.right.right.right == None and root2.right.right.left == None and root2.right.left.right == None)
print(root2.right.left.left.left == None and root2.right.left.left.right == None and root2.right.val == 8)
print("------------------------------------------")
# search
print("search")
print(Solution().search(root2, 10) == root2.right.right)
print("------------------------------------------")
# modify
print("modify")
root4 = Solution().modify(root4, 7, 4)
root = TreeNode(5)
root.left = TreeNode(3)  
root.left.left = TreeNode(3) 
root.left.left.left = TreeNode(-5) 
root.right = TreeNode(8)
root.right.left = TreeNode(7)
root.right.left.left = TreeNode(6)
root.right.right = TreeNode(10)
root = Solution().modify(root,7,4)
print(root.right.left.val)
print(root.left.right.val)
```

    insert
    True
    ------------------------------------------
    delete
    True
    True
    True
    True
    ------------------------------------------
    search
    True
    ------------------------------------------
    modify
    6
    4


# 參考資料：
### https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
### http://alrightchiu.github.io/SecondRound/binary-search-tree-searchsou-xun-zi-liao-insertxin-zeng-zi-liao.html
### https://www.youtube.com/watch?v=f5dU3xoE6ms&t=852s
### https://github.com/tonyforreal/Tony-learning-note/tree/master/HW3
### https://github.com/wellslu/DSA/blob/master/HW3/binary_search_tree_06170107.py
### https://github.com/jay940059/-/blob/master/HW3/binary_search_tree_06170221.py 的modify



```python

```
