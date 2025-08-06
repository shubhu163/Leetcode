# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque()

        if root:
            queue.append(root)
        
        level = 0
        while len(queue)>0:
            level_list=[]
            for i in range(len(queue)):
                curr = queue.popleft()
                level_list.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                if (curr.val % 2) == (level % 2):
                    return False

                if len(set(level_list)) != len(level_list):
                    return False
                if level % 2 ==0:
                    if sorted(level_list) != level_list:
                        return False
                if level % 2==1:
                    if sorted(level_list,reverse=True) != level_list:
                        return False

            level +=1
        return True

        