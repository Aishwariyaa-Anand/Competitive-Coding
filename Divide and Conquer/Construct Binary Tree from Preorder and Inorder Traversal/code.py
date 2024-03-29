# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        root=preorder[0]
        node=TreeNode(root)
        mid=inorder.index(root)
        node.left=self.buildTree(preorder[1:mid+1],inorder[0:mid])
        node.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return node
        
