# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        dummy=newhead=ListNode(0,head)
        temp=head
        while temp:
            while stack and stack[-1].val<temp.val:
                stack.pop()
            stack.append(temp)
            temp=temp.next
        for i in stack:
            newhead.next=i
            newhead=newhead.next
        return dummy.next
        '''temp=head
        while temp.next!=None:
            n1=temp.val
            n2=temp.next.val
            if n2<=n1:
                prev=temp
                temp=temp.next
                print(prev.val,temp.val,1)
            else:
                if prev:
                    prev.next=temp.next
                    temp=prev
                    prev=None
                else:
                    temp=temp.next
        return head'''
