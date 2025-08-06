# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None 
        root = TreeNode(preorder[0])
        mid = len(preorder)
        for i in range(len(preorder)):
            if preorder[i] > preorder[0]:
                mid = i
                break
        root.left = self.bstFromPreorder(preorder[1:mid])
        root.right = self.bstFromPreorder(preorder[mid:])
        return root

        