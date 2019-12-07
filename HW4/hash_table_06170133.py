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
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = int(h.hexdigest(),16)
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
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = int(h.hexdigest(),16)
        y = x%self.capacity
        z = self.data[y]
       
        if self.contains(key) != True:
            return 
        
        else:
            if z.val == x:
                self.data[y] = self.data[y].next
                return 

            else:
                point = self.data[y]
                while point.next.val != x:
                    point = point.next
                point.next = point.next.next
                
    def contains(self, key):
        h = MD5.new()
        h.update(key.encode("utf-8"))
        x = int(h.hexdigest(),16)
        y = x%self.capacity
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
#https://github.com/yunghsin615/little_sun
