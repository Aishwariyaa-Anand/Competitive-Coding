# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1=front=ListNode(0)
        dummy2=back=ListNode(0)
        while head!=None:
            if head.val<x:
                front.next=head
                front=front.next
            else:
                back.next=head
                back=back.next
            head=head.next
        back.next=None
        front.next=dummy2.next
        return dummy1.next