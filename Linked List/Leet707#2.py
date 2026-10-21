class Node:
    def __init__(self,val):
        self.val = val 
        self.prev = None 
        self.next = None  

class MyLinkedList:
    def __init__(self):
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right 
        self.right.prev = self.left 

    def get(self,index: int) -> int:
        itr = self.left.next 
        while itr and index > 0:
            itr = itr.next 
            index -=1 
        if itr and itr!= self.right and index ==0:
            return itr.val 
        return -1 
    def addAtHead(self,val:int) -> int :
        node,prev,next = Node(val),self.left,self.left.next 
        next.prev = node 
        prev.next = node 
        node.next = next 
        node.prev = prev 

    def addAtTail(self,val:int) -> int:
        node,prev,next = Node(val),self.right.prev,self.right 
        next.prev = node 
        prev.next = node 
        node.next = next 
        node.prev = prev 

    def addAtIndex(self,index: int,val:int) -> None:
        itr = self.left.next 
        while itr and index>0:
            itr = itr.next 
            index -= 1
        if itr and index == 0:
            node,prev,next = Node(val),itr.prev,itr 
            next.prev = node 
            prev.next = node 
            node.next = next 
            node.prev = prev 

    def removeAtIndex(self,index: int) -> None: 
        itr = self.left.next 
        while itr and index >0:
            itr = itr.next 
            index -= 1
        if itr and itr!= self.right and index == 0:
            prev,next = itr.prev,itr.next
            next.prev = prev
            prev.next =  next
             