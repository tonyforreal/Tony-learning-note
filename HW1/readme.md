# Homework1 (10/18)
> 作業區

## Quick Sort 
### [解題過程](https://nbviewer.jupyter.org/github/tonyforreal/Tony-learning-note/blob/master/Homework1/quicksort.ipynb)
### [10/25自己重寫一次](https://nbviewer.jupyter.org/github/tonyforreal/Tony-learning-note/blob/master/Homework1/re-quicksort.ipynb)
### 解題觀念：
![](/Homework1/image/quick.png)
> 在一串數列中先拿隨便一個數作為基準值(pivot)，比基準值小的一邊，大的丟另一邊，再對左右數列重複此步驟，直到左右兩邊只剩一個數為止。
### 流程圖：
![](/Homework1/image/quicksort%20flowchart.jpg)
### 解題困難：
> 卡最久的應該是如何讓第一批less[]跟more[]繼續sort下去