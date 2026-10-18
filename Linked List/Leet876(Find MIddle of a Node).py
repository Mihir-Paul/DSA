class Solution:
    def MiddleNode(self,head: ListNode | None)-> ListNode | None:
        itr = head 
        count = 0
        while itr is not None:
            count+=1 
            itr = itr.next 
        itr= head
        for i in range(0,count//2):
            itr = itr.next 
        return itr 