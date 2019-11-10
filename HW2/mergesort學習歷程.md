# 流程圖：

![](/classnote/images/mergesort_ad.jpg)
# 學習歷程：
## Fail1：
* 我的想法是先準備一個answer的list來裝每次比較完後比較小的數，第一步是先分割，mid是整段list的中間值，mid左邊的放在leftlist，mid跟mid右邊的index放在rightlist裡。接著是合併，我在合併的地方卡很久，沒辦法之下我只好去參考https://stackoverflow.com/questions/18761766/mergesort-with-python ，隔日自己在重打一次，但我注意到我的答案又反過來了，於是我又用了上次heapsort學到的list.reverse()。


```python
class Solution(object):
    def merge_sort(self,nums):
        answer = []
        if len(nums) <= 1:
            return nums
        mid = int(len(nums)/2)
        leftlist = self.merge_sort(nums[:mid])
        rightlist = self.merge_sort(nums[mid:])


        while (len(leftlist) > 0) or (len(rightlist) > 0):
            if len(leftlist) > 0 and len(rightlist) > 0:
                if leftlist[0] > rightlist[0]:
                    answer.append(rightlist[0])
                    rightlist.pop(0)
                else :
                    answer.append(leftlist[0])
                    leftlist.pop(0)
            elif len(rightlist) > 0:
                for i in rightlist:
                    answer.append(i)
                    rightlist.pop(0)
            else:

                for i in leftlist:
                    answer.append(i)
                    leftlist.pop(0)
        answer.reverse()
        return answer

a = [3,5,1,7,9,10,-4,6]
Solution().merge_sort(a)

```




    [6, -4, -4, 9, 5, 3, 7, 1]



## Fail2：
* 但我發現因為answer在while底下所以直接reverse會影響到答案，所以我就寫了一個函式專門來reverse答案，總算可以從小到大排。


```python
class Solution(object):
    def merge_sort(self,nums):
        result = self.helper(nums)
        result.reverse()
        return result

    def helper(self, nums):
        answer = []
        if len(nums) <= 1:
            return nums
        mid = int(len(nums) / 2)
        leftlist = self.helper(nums[:mid])
        rightlist = self.helper(nums[mid:])

        while (len(leftlist) > 0) or (len(rightlist) > 0):
            if len(leftlist) > 0 and len(rightlist) > 0:
                if leftlist[0] > rightlist[0]:
                    answer.append(leftlist[0])
                    leftlist.pop(0)
                else:
                    answer.append(rightlist[0])
                    rightlist.pop(0)
            elif len(rightlist) > 0:
                for i in rightlist:
                    answer.append(i)
                    rightlist.pop(0)
            else:

                for i in leftlist:
                    answer.append(i)
                    leftlist.pop(0)

        return answer

a = [3, 2, -4, 6, 4, 2, 19]
Solution().merge_sort(a)

```




    [-4, 2, 2, 3, 4, 6, 19]



## Final Answer:
* 隔日早上我再看一次，我忽然發現我while迴圈的第一個if中，append錯list的第一項，才導致答案是從大到小，於是我又再改一次後最後答案才出來。


```python
class Solution(object):
    def merge_sort(self, nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        answer = [] #創一個空的list裝答案
        if len(nums) <= 1: #如果list等於或小於1，就直接回傳該list
            return nums
        mid = int(len(nums)/2) #先找出中間值在哪，準備拆解list
        leftlist = self.merge_sort(nums[:mid]) #mid左邊的index放在左邊的list
        rightlist = self.merge_sort(nums[mid:]) #mid+右邊的index放在右邊的list


        while (len(leftlist) > 0) or (len(rightlist) > 0):
            if len(leftlist) > 0 and len(rightlist) > 0: #如果兩個list長度都大於0就跑這個
                if leftlist[0] > rightlist[0]: #如果左邊第一個數大於右邊第一個，
                    answer.append(rightlist[0]) #把右邊第一個append到答案的list裡
                    rightlist.pop(0) #把append進去的數從原本的list pop掉
                else :
                    answer.append(leftlist[0]) #else的話就是把左邊的第一個append到答案list裡
                    leftlist.pop(0) #把append進去的數從原本的list pop掉
                    
            elif len(rightlist) > 0: #如果只有右邊的list還有東西就跑這個
                for i in rightlist:
                    answer.append(i) #append出他的數
                    rightlist.pop(0) #pop掉
                    
            else: #如果是左邊list還有東西就跑這邊
                for i in leftlist:
                    answer.append(i) #append出他的數
                    leftlist.pop(0) #pop掉

        return answer
    
a = [3,5,1,7,9,10,-4,6]
Solution().merge_sort(a)
```




    [-4, 1, 3, 5, 6, 7, 9, 10]



# 參考資料：
https://stackoverflow.com/questions/18761766/mergesort-with-python

https://www.youtube.com/watch?v=mB5HXBb_HY8&t=366s


```python

```
