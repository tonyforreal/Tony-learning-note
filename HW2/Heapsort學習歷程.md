# 流程圖：

![](/classnote/images/heapsort_ag.jpg)
# Fail1:
### 這是我看完老師的ppt後第一次打出來的東西，我的想法是先定義一個heapify的函式，其中也定義root跟child，因為我是用Maxheap所以如果parent小於child，則兩者需要換位子。接著第一個for迴圈是作Maxheap，因為是Maxheap的關係所以最下層的child都不會是任何元素的parent，不需要經過heapify;而最上面的root會是最後一位parent，所以for迴圈要在-1的位子停止;方向是-1，所以我的range是設(n//2-1,-1,-1)，每次i的值都要去跑heapify。第二個for迴圈是將Maxheap做排序，目標是從最後一個位子到第二個位子(因為第二個位子排序好之後Maxheap裡面就剩一個數就不需要排序)，所以range設(n-1,0,-1)，把root跟最後一個數做交換，root不看，剩下的tree再進行heapify後繼續把新的root搬下來，重複步驟後list就完成sorting了。

### 失敗原因：主要是因為助教規定的格式下，我想不到該怎麼調整code去讓我設的變數可以在兩個define底下使用。



```python
class Solution(object): 
    def heap_sort(self, nums):
        
        
        def heapify(self,nums,n,i):
            Max = i
            l = 2*i+1
            r = 2*i+2
            n=len(nums)
            if l < n and nums[l] > nums[i]:               
                Max=l
            if r < n and nums[r] > nums[i]:
                Max = r
            if Max != i:
                nums[i],nums[Max] = nums[Max],nums[i]
                heapify(nums,n,Max)
       
        
    for i in range(n//2-1,-1,-1):
        heapify(nums,n,i)
            
    for i in range(n-1,0,-1):
        nums[0],nums[i]=nums[i],nums[0]
        heapify(nums,n,i)            

Solution().heap_sort([3,2,-4,5,4,19])
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-4-8223a500439a> in <module>
    ----> 1 class Solution():
          2     def heap_sort(self, nums):
          3 
          4 
          5         def heapify(self,nums,n,i):


    <ipython-input-4-8223a500439a> in Solution()
         17 
         18 
    ---> 19     for i in range(n//2-1,-1,-1):
         20         heapify(nums,n,i)
         21 


    NameError: name 'n' is not defined


# Fail2:
### 第二次我把第一次程式碼的兩個for迴圈都define成函式，第一個for迴圈改為 def buildheap(self,nums):，第二個for迴圈則改成def sift(self,nums):，而在詢問簡大為同學關於如何在heap_sort時將其他函式加進來後，我學會使用self.函式()的方法。

### 失敗原因：在sift之後我不知道如何將root轉移出Maxheap，導致下一行heapify時又會將root丟回去，進而導致最後的答案錯誤。


```python
class Solution():
    def heap_sort(self, nums):
        self.nums=nums
        heap=self.buildheap(nums)
        sift=self.sift(heap)
        return sift
        
        
    def heapify(self,nums,n,i):
        Max = i
        l = 2*i+1
        r = 2*i+2
        n=len(nums)
        if l < n and nums[l] > nums[i]:               
            Max=l
        if r < n and nums[r] > nums[i]:
            Max = r
        if Max != i:
            nums[i],nums[Max] = nums[Max],nums[i]
            self.heapify(nums,n,Max)
       
    def buildheap(self,nums):
        n=len(nums)
        for i in range(n//2-1,-1,-1):
            self.heapify(nums,n,i)
        return nums    
    
    def sift(self,nums):
        n=len(nums)
        for j in range(n-1,0,-1):
            nums[0],nums[j]=nums[j],nums[0]
            self.heapify(nums,j,0)
        return nums
    
Solution().heap_sort([3,2,-4,5,4,19])
```




    [5, 19, 2, 4, 3, -4]



# Final:
### 無奈之下我只好再次詢問簡大為同學的code，了解後我隔日自己照著想法再打一次，且稍微改變了我與他之間的程式碼，由於簡大為同學的code適用minheap的觀念，我挑戰自己去用Maxheap的觀念試一次，最後我還以為成功打出可以運行的heapsort時卻發現我的list是從大排到小，於是我去網路上查詢如何讓list倒轉過來後，才弄出正確答案。


```python
class Solution(object):
    
    def heap_sort(self,nums): #heap_sort為控制台，將下面設好的funtion一一使用
        answer = [] #創一個空的list裝root
        self.heapify(nums)
        while len(nums) != 0: #list裡面還有東西就繼續跑while
            answer.append(nums.pop(0)) #把root用pop弄到answer=[]裡面
            self.heapify(nums) #剩下的tree可能不會是heap的狀態所以需要再heapify
        
        return answer #把剛root pop 到answer=[]的結果return出來
    
    def getpar(self, ind:int): #找尋每個值的parent在哪
        if ind <= 0: #如果index=0或小於0表示該值沒有parent
            return
        return int((ind+1)/2-1) 
    
    
    def checkup(self, ind: int, arr: list): #比較parent與child
        
        par_ind = self.getpar(ind) #確認parent的index
        if par_ind is None:
            return
        
        self_val = arr[ind]
        par_val = arr[par_ind]
        
        if par_val < self_val: #swap 若parent大於child則換位子(因為是minheap)
            arr[ind] = par_val
            arr[par_ind] = self_val
            
        self.checkup(par_ind,arr)
        
    
    def heapify(self, arr:list): #將輸入的list變成heap(minheap)
        for i in reversed(range(len(arr))): #從大到小開始找
            self.checkup(i,arr) #尋找parent 需要時換位子
            
Solution().heap_sort([3,2,-4,5,4,19])
```




    [19, 5, 4, 3, 2, -4]



# 最終答案：


```python
class Solution(object):
    
    def heap_sort(self,nums): #heap_sort為控制台，將下面設好的funtion一一使用
        answer = [] #創一個空的list裝root
        self.heapify(nums)
        while len(nums) != 0: #list裡面還有東西就繼續跑while
            answer.append(nums.pop(0)) #把root用pop弄到answer=[]裡面
            self.heapify(nums) #剩下的tree可能不會是heap的狀態所以需要再heapify
        answer.reverse()
        return answer #把剛root pop 到answer=[]的結果return出來
    
    def getpar(self, ind:int): #找尋每個值的parent在哪
        if ind <= 0: #如果index=0或小於0表示該值沒有parent
            return
        return int((ind+1)/2-1) 
    
    
    def checkup(self, ind: int, arr: list): #比較parent與child
        
        par_ind = self.getpar(ind) #確認parent的index
        if par_ind is None:
            return
        
        self_val = arr[ind]
        par_val = arr[par_ind]
        
        if par_val < self_val: #swap 若parent大於child則換位子(因為是minheap)
            arr[ind] = par_val
            arr[par_ind] = self_val
            
        self.checkup(par_ind,arr)
        
    
    def heapify(self, arr:list): #將輸入的list變成heap(minheap)
        for i in reversed(range(len(arr))): #從大到小開始找
            self.checkup(i,arr) #尋找parent 需要時換位子
            
Solution().heap_sort([3,2,-4,5,4,19])
```




    [-4, 2, 3, 4, 5, 19]



# 參考資料：
## https://github.com/JetVayne/DSA2019/blob/master/HW2/heap_sort_06170123.py
## https://www.programiz.com/dsa/heap-sort
## https://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
## https://github.com/pecu/DSA/blob/master/06_HeapSort/heapSort.py


```python

```
