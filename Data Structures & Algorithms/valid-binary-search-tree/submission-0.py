# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node, leftLim, rightLim):
            if not node:
                return True
            
            if node.val <= leftLim or node.val >= rightLim:
                return False
            
            return validate(node.left, leftLim, node.val) and validate(node.right, node.val, rightLim)
        
        return validate(root, -math.inf, math.inf)