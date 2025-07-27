# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        
        # def rec(node):
        #     if not node:
        #         return 0

        #     res = 0

        #     if node.left and not node.left.left and not node.left.right:
        #         res += node.left.val

        #     res +=  rec(node.left)
        #     res+= rec(node.right)
        #     return res
        
        # return rec(root)
        
        q = deque()
        q.append(root)
        res = 0
        while q:
            node = q.popleft()
            if node:
                if node.left and not node.left.left and not node.left.right:
                    res += node.left.val
                
                q.append(node.left)
                q.append(node.right)
        return res


