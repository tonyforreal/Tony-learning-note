class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x=None
        self.next=None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if self.x == None:
            self.x=x
        elif self.x != None:
            n=self
            while n.next != None:
                n=n.next
            n.next=MyQueue()
            n.next.x=x
            

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        n=self
        m=self.x
        if n.x != None and n.next == None:
            n.x=None
        elif n.next != None:
            n.x=n.next.x
            n.next=n.next.next
        return m
            

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.x

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.x == None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
