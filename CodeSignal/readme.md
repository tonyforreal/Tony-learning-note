# CodeSignal
> 自主練習python

## 1. ![](/CodeSignal/images/Python%201.png)
### 解析
題目中的 res = [False]*2 會變成 res = [False, False]，而 if xs就是如果xs是對的(因為xs是空的，沒東西可以是False)，則res[0]會變成True也是對的。而第二個 if xs[0]，因為xs是空的，所以xs[0]是False，所以res[1]不變，答案為[True, False]

## 2. ![](/CodeSignal/images/Python%202.png)
### 解析
我答題的想法是題目問說哪個效率最高，我認為選項1的函式最為精簡所以就選1

## 3. ![](/CodeSignal/images/Python%203.png)
### 解析
a == not b是錯的，因為python會先處理==，故正確方式應該為 a == (not b)
