# Merge Sort 

## 原理
Mergesort又稱合併排序，是一種 Divide and Conquer 的演算法，它是將一個 array 分解為幾個 sub array，直到每個 sub array 由一個元素組成，然後以產生排序列表的方式合併這些子列表。

可以分成三個步驟：

1. **切分**: 將未排序的 array 劃分為 sub array，當每個 sub array 就是每個 element 時。
2. **比較合併**: 將相鄰的兩個 sub array ，互相比較第一個 element ，並取較小值則為以排序值，以排序值可以用新 array 存或是用 index 的方式將其隔開。
3. 重複該過程，直到所有 sub array 都合併成一個 array 。
![](/classnote/images/merge.png)


## 時間複雜度
與Heapsort一樣，不論最佳、最糟或平均狀況都為O(nlogn)
