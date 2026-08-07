# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def solve(node):
            hasP = node.val == p.val
            hasQ = node.val == q.val
            if node.left:
                left, hp, hq = solve(node.left)
                if left:
                    return left, hp, hq
                hasP = hp or hasP
                hasQ = hq or hasQ
            if node.right:
                right, hp, hq = solve(node.right)
                if right:
                    return right, hp, hq
                hasP = hp or hasP
                hasQ = hq or hasQ

            if hasP and hasQ:
                return node, hasP, hasQ
            return None, hasP, hasQ

        return solve(root)[0]