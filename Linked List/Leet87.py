class Node:
    def __init__(self,val,next):
        self.val = val 
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Node | None) -> Node | None: 
        itr = self.head 
        while itr and itr.next:
            if itr.val == itr.next.val:
                itr.next = itr.next.next 
            else:
                itr = itr.next 

        return itr
                  