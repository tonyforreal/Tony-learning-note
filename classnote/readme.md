# 目錄：
* [Stack&Queue](#stackqueue)
   * [Stack](#stack-必須有的功能)
   * [Queue](#queue-必須有的功能)
* [Insertion Sort](#insertion-sort)
* [Heap Sort](#heap-sort)


# Stack&Queue

## Stack 必須有的功能
* **Push(Data)**: 把資料放到最上面(最新)。
* **Pop**: 把資料從最上面(最新)移除。
* **Top**: 回傳最上面(最新)的資料。
* **IsEmpty**: 確認stack 裡面是否有資料。
* **getSize**: 回傳stack 裡的資料個數。

## Queue 必須有的功能
* **Push(Data)**: 把資料放到 Queue 的後面，並更新成新的 back。
* **Pop(dequeue)**: 把 front 所指向的資料從 Queue 中移除，並更新front。
* **getFront**: 回傳 front 所指向的資資料。
* **getBack**: 回傳 Back 所指向的資資料。
* **IsEmpty**: 確認 Queue 裡是否有資料。
* **getSize**: 確認 Queue 裡的資料個數。

# Insertion Sort
## 步驟
1. 第一個(最左邊)的數字直接做為已排序的頭。
1. 將下一個值(右邊)作為基準值。
1. 與所有已排序中的數字比對(右->左)。
1. 移動所有比基準值大的數字。
1. 插入基準值。
1. 回到第2個步驟。
## python符號(補充)
|python 符號|意思|
|:-:|:-|
|---|差集|
|&|交集|
|I|聯集|
|!=|不等於|
|==|等於|
|in|屬於|
|not in|不屬於|

# Heap Sort

## Heap:
> Heap的結構可以視作Complete Binary Tree
* 其**left child**必定位在index(2i)
* 其**right child**必定位在index(2i+1)
* 其**parent**必定位在index(⌊i/2⌋)
## MaxHeapify:

`MaxHeapify()`的功能，是要「由上而下」地，以Max Heap的規則(**root**的數值「大於」兩個**child**的數值)，調整矩陣。

以為例，觀察subtree「index(2)-index(4)-index(5)」之「數值」：

* root：index(i=2)為1
* leftchild：index(2i=4)為9
* rightchild：index(2i+1=5)為4

不符合Max Heap規則，所以要想辦法把這三個數值中的「最大值」，調整到index(i=2)，也就是這棵subtree的**root**。

方法如下：

* 找到這三者的最大值，並以`int largest`記錄該最大值的index。
* 把`largest`記錄為index(4)，將index(root)與index(largest)這兩個node互換位置，如此一來，當前的subtree必定能滿足Max Heap規則。
    * 下圖中，將index(2)與index(4)的node互換。![](/classnote/images/heap1.png)
    * subtree「index(2)-index(4)-index(5)」的數值分別為「9-1-4」，符合Max Heap。
* 繼續以index(largest)當作新的subtree的root，檢查新的subtree是否符合Max Heap規則。
    * 下圖中，subtree「index(4)-index(8)-index(9)」再次不滿足Max Heap。![](/classnote/images/heap2.png)
* 重複上述步驟，將index(4)與index(9)的node互換，得到下圖。
 ![](/classnote/images/heap3.png)
 
> 如此一來，有被`MaxHeapify()`檢查過的subtree，都會符合Max Heap規則。因此，只要對所有「具有child的node」檢查一次`MaxHeapify()`，便能夠把一個任意矩陣調整成Max Heap。





