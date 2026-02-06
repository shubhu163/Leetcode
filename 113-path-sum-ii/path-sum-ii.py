class Solution(object):
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node, path, curSum):
            if not node:
                return

            path.append(node.val)
            curSum += node.val

            if not node.left and not node.right and curSum == targetSum:
                result.append(list(path))  # copy!

            dfs(node.left, path, curSum)
            dfs(node.right, path, curSum)

            path.pop()  # backtrack

        dfs(root, [], 0)
        return result
