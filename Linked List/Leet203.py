class ListNode:
    def __init__(self,val,next=None):
        self.val = val 
        self.next = next 



class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0,head)
        prev,curr = dummy,head 

        while curr:
            nxt = curr.next 

            if curr.val == val:
                prev.next = nxt 
            else:
                prev = curr 
            curr = nxt 
        return dummy.next