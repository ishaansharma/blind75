# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if not root: return 0
        if not root.right and not root.left: return root.val
        self.globalmax = float('-inf')
        
        def get_path(node):
            if not node: return 0
             
            left = max(get_path(node.left), 0)
            right = max(get_path(node.right), 0)
            self.globalmax = max(self.globalmax, left + right + node.val)
            
            return max(node.val + left, node.val + right)
        
        get_path(root)
        return self.globalmax
        