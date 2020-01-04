# Hash table
## Hash table
hash table 是一個資料結構，用來儲存一對 keys & value 。他使用 hash function 將 key 轉換成 array 對應的位置(index) 。而該位置就是用來儲存 value 的。
使用的 hash function 好壞是 hash table 關鍵。 在一般情況下，hash table 搜尋特定的物件的時間複雜度平均為 O(1)

## Hashing
現實生活中的例子:
1. 在學校裡，每位學生都有特定的編號，這編號可以用來查詢他的相關資料。
2. 在圖書館裡，每本書都有一個特別編號，紀錄與該書本相關的資訊，像是類別、借還書資料 之類的...

上述兩種情況都會需要有特別編碼(unique number)。簡單來講就是他是一個將 key 轉成 index 的工作。而要如何用程式去實現呢? 我們把輸入值(str)當作 key ，然後透過 MD5 的 hexdigest() 將字串轉換成 16 進位的格式，在透過 hash function 轉換成對應的 index 。

## Hash function
hash function 可以把不規則的資料(像是字串)轉成特定index(在有限的 array_size 下) 然後會存入 hash table。從 hash function 出來的值稱作 hash values、hash codes、hash sums 或是 simply hashes。

一個好的 hashing 機制 ，需要一個好的 hash function ，他有以下幾個特點

- easy to computing (很好計算): 他不是一個複雜的演算法，必須能夠簡單快速的轉換。

- Uniform distribution (均勻分布): 他必須均勻分布，不要只偏向某格群體(index)，這樣會影響 hash table 的效率.

- Less collisions (少碰撞):碰撞就是有兩個 key 會對應到同個 hash value(index)，這是要避免的。



## MD5 Hash
This hash function accepts sequence of bytes and returns 128 bit hash value, usually used to check data integrity but has security issues.

Functions associated :
* encode() : Converts the string into bytes to be acceptable by hash function.
* digest() : Returns the encoded data in byte format.
* hexdigest() : Returns the encoded data in hexadecimal format.
