# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()

        if root:
            queue.append(root)
        
        res = []
        flag = True
        while queue:
            arr = []
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    arr.append(curr.val)

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if flag == True:
                res.append(arr)
            else:
                arr2 = []
                for i in range(len(arr)-1,-1,-1):
                    arr2.append(arr[i])
                res.append(arr2)
            flag = not flag
        
        return res
                
        