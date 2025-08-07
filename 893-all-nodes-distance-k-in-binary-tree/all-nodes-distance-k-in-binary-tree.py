# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)

        def buildgraph(node,parent=None):
            if not node:
                return 
            if parent:
                graph[node.val].append(parent.val)
                graph[parent.val].append(node.val)
            buildgraph(node.left,node)
            buildgraph(node.right,node)
        buildgraph(root)

        visited = set()
        queue = deque()
        queue.append([target.val,0])
        visited.add(target.val)
        res = []

        while queue:
            node,dist = queue.popleft()
            if dist == k:
                res.append(node)
            elif dist <k:
                for n in graph[node]:
                    if n not in visited:
                        visited.add(n)
                        queue.append([n,dist+1])
        
        return res



