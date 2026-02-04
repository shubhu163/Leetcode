# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if not root:
            return []
        
        else:

            queue = deque([root])
            level = 0
            result = []

            while len(queue) >0:
                result.append([])
                for i in range(len(queue)):
                    curr = queue.popleft()
                    result[level].append(curr.val)
                    if curr.left:
                        queue.append(curr.left)
                    if curr.right:
                        queue.append(curr.right)
                level+=1

            return result
        







