
# Hash Table原理：
### Hash Table是把Key通過一個固定的算法函數經過hash funtion轉換成一個整型數字，然後就將該數字對數組長度進行取餘，取餘結果就當作數組的下標，將value存儲在以該數字為下標的數組空間裡。hash funtion可以自己define，但我們這次是利用別人寫的MD5來作加密的過程，而MD5是十六進位，而我們再加上int()的話就變成十進位的純數字密碼，而同一個str經過MD5都會跑出一樣的密碼。接著是把生成的密碼加進table裡，利用密碼去除以table抽屜個數的餘數可以判斷出該密碼要放置在哪一層抽屜裡，如果兩段密碼的餘數相等，則利用linked list的方式把兩段密碼接在一起並放在同一層抽屜裡。

# Hash Funtion原理：
### 主要是將不定長度的字串或數字的輸入，演算成固定長度雜湊值的輸出，且輸出的雜湊值是無法反推出原來的訊息的，想像hash funtion是一個果汁機，把很多水果種類丟進去打成汁後，倒出來的果汁是無法回推成原來的水果的，hash funtion生出的雜湊值也無法回推原來輸入的字串或數字。但也會有出狀況的時候，有可能兩個不同的輸入字串在經過雜湊運算後得到同樣的結果，也就是兩者都存在同一層抽屜裡，這就是雜湊碰撞。而其中一種解決辦法是利用linked list把同一層抽屜的資料串串起來，或是直接增加抽屜層數都是可行辦法。
# 流程圖：


# 學習歷程：
## contains:
### 一開始我還是決定從搜尋開始，因為感覺hash的刪除會用到搜尋的功能。
### 先用老師教的MD5把key換成密碼並int且設他為x ; x除以capacity的餘數(也就是x要放的抽屜層數)設為y。尋找會碰到的狀況會有兩種，一種是table裡有要找的node，一種是沒有，而有要找的node又會有兩種狀況，如果該層抽屜裡有不只一個node，就要繼續往後找直到我們要尋找的目標與table內的node一致為止。


```python
def contains(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x % self.capacity
        z = self.data[y]
        
        while z:
            if z.val is not x:
                z = z.next
            else:
                return True
        
        return False
```

## add:
### 這裡就可以用到剛剛寫好的contains了
### MD5的部分都一樣，然後我的想法是先利用contains確認table裡有沒有要加入的node，如果有就不重複加了因為助教有說可以不用重複加。
### 如果沒有，首先先確認該層抽屜有沒有node在裡面了，如果有，就要把原本的推到next的位子後再把要加入的node放進來。


```python
def add(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        
        if self.contains(key) is not True:
            if self.data[y] is not None:
                new = ListNode(x)
                new.next = self.data[y]
                self.data[y] = new
            else:
                self.data[y] = ListNode(x)
        else:
            return
```

## 測試：
### 原本想說來測試一下add跟contains，沒想到發現一個蠻怪的問題


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def add(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        
        if self.contains(key) is not True:
            if self.data[y] is not None:
                new = ListNode(x)
                new.next = self.data[y]
                self.data[y] = new
            else:
                self.data[y] = ListNode(x)
        else:
            return
    
    def contains(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x % self.capacity
        z = self.data[y]
        
        while z:
            if z.val is not x:
                z = z.next
            else:
                return True
        
        return False
    
hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("dog")
print(rel)
```

    False
    False


### 看了很多次程式碼後我還是找不到問題在哪，我是亂猜亂改才發現如果我把if else裡的is或is not改成==或!=就可以跑了，到現在我還是不大懂原因，但好在亂改有改中


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def add(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        
        if self.contains(key) != True:
            if self.data[y] != None:
                new = ListNode(x)
                new.next = self.data[y]
                self.data[y] = new
            else:
                self.data[y] = ListNode(x)
        else:
            return
        
    def contains(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x % self.capacity
        z = self.data[y]
        
        while z:
            if z.val != x:
                z = z.next
            else:
                return True
        
        return False
    
hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("dog")
print(rel)
```

    True
    True


## remove:
### 這是我想最久的一部分，一樣先MD5，我的想法一樣是先用contains確認table裡有沒有要刪掉的node，有的話把要刪的Node與next的Node變成一樣，然後把其中一個改成None就可以把該Node刪除了，如果沒有next就直接把該Node轉成None。


```python
def remove(self, key):
        if self.contains(key) == True:
            x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
            y = x%self.capacity
            z = self.data[y]
            
            if z.val == x:
                if z.next is True:
                    self.data[y] = self.data[y].next
                    self.data[y].next == None
                else:
                    self.data[y] = None
        
            else:
                while z.next.val != x:
                    z = z.next
                    
        else:
            return
        

```


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def remove(self, key):
            if self.contains(key) == True:
                x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
                y = x%self.capacity
                z = self.data[y]

                if z.val == x:
                    if z.next is True:
                        self.data[y] = self.data[y].next
                        self.data[y].next == None
                    else:
                        self.data[y] = None

                else:
                    while z.next.val != x:
                        z = z.next

            else:
                return
            
    def add(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        
        if self.contains(key) != True:
            if self.data[y] != None:
                new = ListNode(x)
                new.next = self.data[y]
                self.data[y] = new
            else:
                self.data[y] = ListNode(x)
        else:
            return
    
    def contains(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x % self.capacity
        z = self.data[y]
        
        while z:
            if z.val != x:
                z = z.next
            else:
                return True
        
        return False


hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
hashSet.add("sie")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("sie")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("dog")
rel = hashSet.contains("dog")
print(rel)
```

    True
    True
    True
    False
    True
    True


### 但我發現如果我故意找兩個餘數相同的str新增進去後，我的程式碼會無法把想刪的node刪掉，而我也反覆測試修改後還是沒辦法，所以我就直接放棄這段寫一個新的。


```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def remove(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        z = self.data[y]
       
        if self.contains(key) != True:
            return 
        
        else:
            if z.val == x:
                self.data[y] = self.data[y].next
                return 

            else:
                point = self.data[y]
                while point.next.val != x:
                    point = point.next
                point.next = point.next.next
            
    def add(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        
        if self.contains(key) != True:
            if self.data[y] != None:
                new = ListNode(x)
                new.next = self.data[y]
                self.data[y] = new
            else:
                self.data[y] = ListNode(x)
        else:
            return
    
    def contains(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x % self.capacity
        z = self.data[y]
        
        while z:
            if z.val != x:
                z = z.next
            else:
                return True
        
        return False


hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
hashSet.add("sie")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("sie")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("dog")
rel = hashSet.contains("dog")
print(rel)
```

    True
    True
    True
    False
    True
    False


### 新的一段程式碼我保留用contains確認table有沒有要刪的node，以及把self.data[y]改成self.data[y].next後把一個轉成None的想法，最後竟然可以跑出正確答案，那可能是我第一段太過雜亂，導致我自己也找不到錯在哪

## final form:



```python
from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def add(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        
        if self.contains(key) != True:
            if self.data[y] != None:
                new = ListNode(x)
                new.next = self.data[y]
                self.data[y] = new
            else:
                self.data[y] = ListNode(x)
        else:
            return
        
    def remove(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        z = self.data[y]
       
        if self.contains(key) != True:
            return 
        
        else:
            if z.val == x:
                self.data[y] = self.data[y].next
                return 

            else:
                point = self.data[y]
                while point.next.val != x:
                    point = point.next
                point.next = point.next.next
                
    def contains(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x % self.capacity
        z = self.data[y]
        
        while z:
            if z.val != x:
                z = z.next
            else:
                return True
        
        return False
    
hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
hashSet.add("sie")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("sie")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("dog")
rel = hashSet.contains("dog")
print(rel)
    
#參考資料：
#https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash
#https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-ae8becaf165e
#https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
#https://github.com/yunghsin615/little_sun
#https://github.com/tonyforreal/Tony-learning-note
```

    True
    True
    True
    False
    True
    False


# 參考資料：
## https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash
## https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-ae8becaf165e
## https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
## https://github.com/yunghsin615/little_sun
## https://github.com/tonyforreal/Tony-learning-note
