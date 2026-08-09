# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = 0
        def dfs(node):
            nonlocal curr
            if not node:
                return
            
            left = dfs(node.left)

            curr += 1
            if curr == k:
                return node.val

            right = dfs(node.right)
            if left:
                return left
            if right:
                return right
        
        return dfs(root)


        