# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack,answer=[],[]
        pos=-1
        while head:
            pos+=1
            answer.append(0)
            while stack and stack[-1][1]<head.val:
                ind,val=stack.pop()
                answer[ind]=head.val
            stack.append((pos,head.val))
            head=head.next
        return answer
