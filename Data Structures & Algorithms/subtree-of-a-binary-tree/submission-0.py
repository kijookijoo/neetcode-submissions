# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def compare(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            
            return compare(p.right,q.right) and compare(p.left,q.left) and p.val == q.val
        
        if not root:
            return False
        
        return compare(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
        