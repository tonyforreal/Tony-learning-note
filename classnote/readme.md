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

## python符號
|:-:|:-|
|---|差集|
|&|交集|
|I|聯集|
|!=|不等於|
|==|等於|
|in|屬於|
|not in|不屬於|
