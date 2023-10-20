class node:
     
    def __init__(self, value):
        self.data = value
        self.next = None
t1 = node(10)
t2 = node(20)
t3 = node(30)
t1.next = t2
t2.next = t3
head = t1
        
    
         
    