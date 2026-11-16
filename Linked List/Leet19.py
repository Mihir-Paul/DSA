class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0,head)
        left,right = dummy,head 
        while n>0 and right:
            right = right.next 
            n -=1 
        while right:
            left = left.next 
            right = right.next 

        left.next = left.next.next 
        return dummy.next