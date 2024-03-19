# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        c=1
        x=[]
        temp=head
        while temp and temp.next:
            c+=1
            temp=temp.next
        div=c//k
        mod=c%k
        temp=head
        for i in range(k):
            dummy=write=ListNode()
            for j in range(div+(i<mod)):
                if temp:
                    write.next=write=ListNode(temp.val)
                    temp=temp.next
            x.append(dummy.next)
        return x    
