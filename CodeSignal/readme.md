# CodeSignal
> 自主練習python

## 1. ![](CodeSignal/images/Python 1.png)
題目中的 res = [False]*2 會變成 res = [False, False]，而 if xs就是如果xs是對的(因為xs是空的，沒東西可以是False)，則res[0]會變成True。而第二個 if xs[0]，因為xs是空的，所以xs[0]是False，所以res[1]不變，答案為[True, False]
