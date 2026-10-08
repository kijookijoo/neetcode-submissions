# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            return p.val == q.val and compare(p.left, q.left) and compare(p.right, q.right)
        
        if not root:
            return False
        
        if root.val == subRoot.val:
            if compare(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        