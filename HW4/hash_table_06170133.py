from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
    
    def add(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x%self.capacity
        
        if self.contains(key) != True:
            if self.data[y] != None:
                new = ListNode(x)
                new.next = self.data[y]
                self.data[y] = new
            else:
                self.data[y] = ListNode(x)
        else:
            return
        
    def remove(self, key):
        if self.contains(key) == True:
            x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
            y = x%self.capacity
            z = self.data[y]
            
            if z.val == x:
                if z.next is True:
                    self.data[y] = z.next
                else:
                    self.data[y] = None
        
            else:
                while z.next.val != x:
                    z = z.next
                    
        else:
            return
        
    def contains(self, key):
        x = int(MD5.new(key.encode("utf-8")).hexdigest(),16)
        y = x % self.capacity
        z = self.data[y]
        
        while z:
            if z.val != x:
                z = z.next
            else:
                return True
        
        return False
        
        
#參考資料：
#https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash
#https://medium.com/ccclub/ccclub-python-for-beginners-tutorial-ae8becaf165e
#https://www.nosuchfield.com/2016/07/29/the-python-implementationp-of-HashTable/
#https://github.com/tonyforreal/Tony-learning-note
