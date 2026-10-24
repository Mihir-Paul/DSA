class Node:
    def __init__(self,val,next):
       self.val = val
       self.next = next 



class Solution:
    def reverseList(self, head: Node | None) -> Node | None:
        temp = head 
        prev = None 
        while temp:
            first = temp.next 
            temp.next = prev
            prev = temp 
            temp = first

        return prev