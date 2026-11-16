class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if not head or not head.next:
            return 0 

        slow,fast = head,head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 

        second = slow.next 
        second.next = None 

        prev = None 
        while second:
            tmp = second.next 
            second.next = prev 
            prev = second 
            second = tmp 

        first,second = head,prev 
        while first and second:
            tmp1 = first.next 
            tmp2 = second.next 

            first.next = second 
            second.next = tmp1 

            first = tmp1
            second = tmp2