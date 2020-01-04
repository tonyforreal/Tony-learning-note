# Quick Sort

## 原理
從 array 中抽取一個數字為 pivot（基準點），將整個 array 依基準點分成兩個小的 array, 比基準點大的放在右邊的array，比基準點小的放在左邊的array，之後左右兩邊的小array 繼續重複同樣到動作（找基準->分兩邊）直到該小array剩下一個為未排序（未當過基準點）。

![](/HW1/image/quick.png)

> 他有四種方式

- 總是以第一個 element 為基準點
- 總是以最後一個 element 為基準點
- 以中位數為基準點
- 隨機基準點

## 複雜度分析
- 時間複雜度
    - 最差: O(n＾2)

    - 最佳: O(nlogn)

    - 平均: O(nlogn)
