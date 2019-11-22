class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
         self.sear = None
         self.node = None
         self.target = None

    def insert(self, root, val):
        if root is None:
            root = TreeNode(val)
            return root
        else:
            return self.insert_again(val, root)

    def insert_again(self, val, current):
        if val <= current.val:  # 目前的current.val是self.root
            if current.left is None:  # 如果root左下沒有數則把帶入的數變成左邊的小孩
                current.left = TreeNode(val)
                return current.left
            else:
                return self.insert_again(val, current.left)  # 如果有的話則再跑一次insert_again讓他判斷val比左邊小孩大還小
        else:
            if current.right is None:
                current.right = TreeNode(val)
                return current.right
            else:
                return self.insert_again(val, current.right)

    def search(self, root, target):
        if root.val == target:
            return root
        elif root.val < target:
            return self.search(root.right, target)
        elif root.val > target:
            return self.search(root.left, target)
        else:
            return None

    def switch(self,root):
        if root.right is None and root.left is None:
            return None
        elif root.right is not None and root.left is not None:
            x = root.left
            while x.right is not None:
                x = x.right
            root.val = x.val
            root.left = self.delete(root.left,root.val)
            return root
        elif root.right is not None and root.left is None:
            x = root.right
            while x.left is not None:
                x = x.left
            root.val = x.val
            root.right = self.delete(root.right,root.val)
            return root
        elif root.right is None and root.left is not None:
            x = root.left
            while x.right is not None:
                x = x.right
            root.val = x.val
            root.left = self.delete(root.left,root.val)
            return root
        
    def delete(self, root, target):
        if self.target is None:
            self.target = target
        if target < root.val:
            if root.left is None:
                return None
            else:
                root.left = self.delete(root.left, target)
                return root
        elif target > root.val:
            if root.right is None:
                return None
            else:
                root.right = self.delete(root.right, target)
                return root
        elif root.val == target:
            root = self.switch(root)
            if root is not None and root.val == self.target:
                root = self.switch(root)
            return root
        
    def modify(self, root, target, new_val):
        x = 0 
        y = self.search(root,target) 
        if y is not None and y.val == target: 
            x = x + 1 
            y = y.left 
        elif y is None:
            return None
        
        self.delete(root,target) 
        
        for i in range(x): 
            self.insert(root,new_val)
        return root
