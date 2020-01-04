# Heap Sort

## Heap 
Heap(Binary Heap) 是以 tree(樹) 為基礎的資料結構, 他有以下特點:

* Shape Property: Heap 的資料結構永遠都是 `完全二元樹  Complete Binary Tree`, 也就是在每個 level(層級) ，由左至右都有 Node(節點)，但是如果是同層級的左至右中間少一個結點，就不是完全二元樹了。

* Heap Property: 所有節點再初始狀態下沒有大小排序. 但是當所有 parent nodes(父節點)> 所有的 child nodes(子節點), 就會稱作 `Max-Heap`。反之當所有 parent nodes(父節點)< 所有的 child nodes(子節點) `Min-Heap`。

假設index 從0開始，父節點在 index=a 的位置則:
- 左子節點 = 2 x a + 1 
- 右子節點 = 2 x a + 2

## Heap Sort Algorithm for sorting in increasing order:

1. 將 array 轉換成 Maxheap 。
2. 此時 root 的值為 max 。將 root 值與最後一個 index 的值互換，然後將heap 的大小 -1 ，也就是把排序過最大的值丟到 array後面，使其index不再之後處理的範圍內。
3. 重複以上動作，直到 heap 的大小 =1(剩下一個 element)。
![](/classnote/images/BuildMaxHeap.gif)

## 時間複雜度
時間複雜度不論是最佳或最糟或平均狀況都為 O(nlogn)



