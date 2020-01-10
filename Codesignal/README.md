# Codesignal
> 自主練習python

## 1. ![](/Codesignal/image/Python%201.png)
### 解析
題目中的 res = [False]*2 會變成 res = [False, False]，而 if xs就是如果xs是對的(因為xs是空的，沒東西可以是False)，則res[0]會變成True也是對的。而第二個 if xs[0]，因為xs是空的，所以xs[0]是False，所以res[1]不變，答案為[True, False]

## 2. ![](/Codesignal/image/Python%202.png)
### 解析
我答題的想法是題目問說哪個效率最高，我認為選項1的函式最為精簡所以就選1

## 3. ![](/Codesignal/image/Python%203.png)
### 解析
a == not b是錯的，因為python會先處理==，故正確方式應該為 a == (not b)

## 4. ![](/Codesignal/image/Python%204.png)
### 解析
Java中的(/)結果是除法中的商，且只取整數位;Python中的(//)則是會將取到的商的小數位無條件取小一位整數(也就是往負的方向進位)，所以15/-4=-3但15//-4=-4

## 5. ![](/Codesignal/image/Python%205.png)
### 解析
n.bit_length()為python求二進位的長度

## 6. ![](/Codesignal/image/Python%206.png)
### 解析
題目其實是要我們分辨變數n是不是整數，是的話return n除以2的餘數，不是就return -1，而我打的n%1==0就是為了判斷n是不是整數，一旦n除以1的餘數為0的話就表示n一定是整數。

## 7. ![](/Codesignal/image/Python%207.png)
### 解析
在網路上以及某次課堂作業中學到`sorted()`來排序的寫法，把arr先sort過後發現答對了。

