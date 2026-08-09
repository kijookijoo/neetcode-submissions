# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None
        def dfs(node):
            nonlocal ans
            if not node:
                return 
            
            
            if (p.val <= node.val and q.val >= node.val) or (p.val >= node.val and q.val <= node.val):
                return node
            
            left, right = dfs(node.left), dfs(node.right)
            if left:
                return left
            if right:
                return right
    
        return dfs(root)
            
        

        