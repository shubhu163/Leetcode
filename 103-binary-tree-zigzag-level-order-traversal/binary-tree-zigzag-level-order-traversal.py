class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []
        count = 0

        while queue:
            count += 1
            level_size = len(queue)
            arr = []

            for _ in range(level_size):
                node = queue.popleft()
                arr.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if count % 2 == 0:
                arr.reverse()
            res.append(arr)

        return res