

```python
def quicksort(x):
      #如果數列中的數字不到兩個就不用跑下面的程式碼
      if len(x) < 2:
          return x
      else:
          pivot = x[0]#統一用數列的第一個數作為pivot，比pivot小的放less[]裡，大的放more[]裡
          less = [i for i in x[1:] if i <= pivot]
          more = [i for i in x[1:] if i > pivot]
          return quicksort(less) + [pivot] + quicksort(more)#將新的數列重整，若less[]與more[]中還有兩個或以上的數字，則重複分類一次
          #直到所有list中都只剩下一個數，就會停止分類
```


```python
Alist=[4,7,3,0,9,8,5,1,6,2]
```


```python
quicksort(Alist)
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]




```python

```


```python

```