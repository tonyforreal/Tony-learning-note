# 花費時間:
* **兩者在速度上都為nlog(n)，不論是最佳情況、平均情況、或是最糟情況，所花費的時間皆相同。**
# 差別:
## 排列方式
### Heapsort:
* **Heapsort的結構Binary Tree結構有兩種分別是Maxheap與minheap，Maxheap是最大值在nums[0]的位子，且child永遠比parent小，minheap則相反。而Heapsort的排列方式為先將輸入的數列排成一個heap，將root取出後重新排列一次直到剩餘元素符合heap的結構，重複取出root以及heapify動作直到tree裡面沒有元素，便完成sorting。**

### Mergesort:
* **Mergesort則是透過不斷拆解數列直到拆解後的數列中只剩下一個元素，再進行排序後合併，有點像是升級遊戲，將小list與其他小list排序合併之後，再去找同層級的list繼續排序合併，直到合併完成最大的list時，便完成sorting。**
