class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.x=None  
        self.next=None    

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self.x == None:       
            self.x=x        
        else:   
            n=self                 
            while n.next != None:     
                n=n.next                      
                                                     
            n.next=MyStack()         
            n.next.x=x           
            
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        n=self           
        while n.next != None and n.next.x != None: 
            n=n.next     
        m = n.x           
        n.x=None
        return m 
        
    def top(self) -> int:
        """
        Get the top element.
        """
        if self.x == None:               
            return None        
        elif self.x != None:   
            n=self                   
            while n.next != None and n.next.x != None:      
                n=n.next   
        return n.x    

    def empty(self) -> bool:  
        return self.x == None    
