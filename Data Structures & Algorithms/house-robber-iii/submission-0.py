# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        from functools import cache
        @cache
        def f(node, parentRobed):
            if not node:
                return 0
            
            if parentRobed:
                return f(node.left, False) + f(node.right, False)
            else:
                rob = node.val + f(node.left, True) + f(node.right, True)
                no = f(node.left, False) + f(node.right, False)
                return max(rob, no)

        return f(root, False)