# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, greatest):
            if not node:
                return 0
            
            curr = 1 if node.val >= greatest else 0
            
            greatest = max(greatest, node.val)
        
            return dfs(node.left, greatest) + dfs(node.right, greatest) + curr
        
        return dfs(root, -math.inf)
            
