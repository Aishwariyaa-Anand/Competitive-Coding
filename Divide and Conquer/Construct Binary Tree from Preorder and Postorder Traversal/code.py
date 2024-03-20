# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not postorder:
            return None
        node=TreeNode(preorder[0])
        if len(preorder)==1:
            return node
        leftroot=preorder[1]
        left=postorder.index(leftroot)+1
        node.left=self.constructFromPrePost(preorder[1:left+1],postorder[:left])
        node.right=self.constructFromPrePost(preorder[left+1:],postorder[left:-1])
        return node
