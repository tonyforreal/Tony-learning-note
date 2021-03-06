# Insertion Sort
適合用在小筆資料，資料筆數過大會大幅降低它的效率

### 作法
分成已排序 (小 -> 大) 和未排序兩部分。依序由未排序中的第一筆為基準值(正處理的值)，插入到已排序中的適當位置。
* 直到遇到 `第一個 < 基準值` 的值，停止並插入在該值右邊。
* 遇到 `> or = 基準值` 的值，將該值往右移動，基準值繼續往前比較。

### 時間複雜度
* **Best Case：Ο(1)**
    
* **Worst Case：Ο(n2)**
    
* **Average Case：Ο(n2)**


### 步驟
1. 第一個(最左邊)的數字直接做為已排序的頭。
2. 將下一個值(右邊)作為基準值。
3. 與所有已排序中的數字比對(右->左)。
4. 移動所有比基準值大的數字。
5. 插入基準值。
6. 回到第2個步驟。

![](/classnote/images/insertionsort.gif)

