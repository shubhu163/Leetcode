# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        def dfs(node,count):
            if node:
                count +=1
            if not node:
                return count
            
            left = dfs(node.left,count)
            right = dfs(node.right,count)

            return max(left,right)
        
        return dfs(root,0)
        