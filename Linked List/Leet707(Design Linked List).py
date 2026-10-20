class Node:
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = Node(0)
        self.size = 0 

    def get(self,index:int) ->int:
        if index <0 or index >=self.size:
            return -1 

        itr = self.head.next 
        for _ in range(index):
            itr = itr.next 

        return itr.val 

    def addAtHead(self,val: int) -> None:
        self.addAtIndex(0,val)

    def addAtTail(self,val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self,index:int,val:int ) -> None:
        if index<0:
            return 0 

        if index>self.size:
            return 

        itr=self.head 
        for _ in range(index):
            itr = itr.next 
        new_node = Node(val,itr.next )
        itr.next = new_node 

        self.size+=1

    def removeAtIndex(self,index:int) -> None:
        if index<0 and index>=self.size:
            return 0 

        itr = self.head 
        for _ in range(index):
            itr = itr.next 

        itr.next = itr.next.next 

        self.size -=1