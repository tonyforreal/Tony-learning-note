class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x=None #.x就是self當下的那個值
        self.next=None#None表示裡面是空的

    def push(self, x: int) -> None:#push就是把數字加進來，x: int是輸入要加的數字
        """
        Push element x to the back of queue.
        """
        if self.x == None:#如果self裡面是空的話，就直接把要加的數字設成self.x就好了，所以加進來的數字就變成self.x => self.x=x 
            self.x=x 
            #舉例：假如我要加一個數字0，x: int的x就會＝0，啊我self.x裡面沒有東西，所以把0加進來self.x就會從原本的None變成0(0也就是x: int的x)
        elif self.x != None:#如果self.x不是空的
            n=self#設self是一個代號n
            while n.next != None:#如果n的下一個也不是空的，跑一個while迴圈，
                n=n.next#要把原本的n改成n.next，原本的n.next就變成n.next.next
                #舉例：假設self裡面有0跟1，我要加2進來，因為n.next＝1不是空的(n.next!=None)所以要跑while那行
                #n=n.next：原本0是n，1是n.next，現在加2進來，2就變成n.next.next，但不可能一直加next加到底所以我們把原本的n.next變成n，也就是1變成n，這樣2就會變成n.next了
            n.next=MyQueue()
            n.next.x=x
            #所以現在n.next.x就是2了，也就是你要加進來的數字x: int的x => n.next.x=x

    def pop(self) -> int:#刪掉最上面的數字
        """
        Removes the element from in front of queue and returns that element.
        """
        n=self#一樣設self是n
        m=self.x#self.x是m
        if n.x != None and n.next == None: #如果裡面只有一個數字就是n自己的話
            n.x=None #把n刪掉
        elif n.next != None: #如果n.next還有數字
            n.x=n.next.x #這裡就跟上面push是一樣觀念
            n.next=n.next.next
        return m#傳回新的self.x的值
            

    def peek(self) -> int:#他要self裡面的第一個數，也就是最底下的那個
        """
        Get the front element.
        """
        return self.x#假設我的linked list是(0,1,2,3,4)他要的是0，也就是self.x

    def empty(self) -> bool:#如果他要你的結果是self是空的
        """
        Returns whether the queue is empty.
        """
        return self.x == None#那self.x就是None了


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
