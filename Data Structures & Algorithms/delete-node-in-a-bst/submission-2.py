# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.minMax = {}
        
    def computeMinMax(self, node):
        if not node:
            return None
        self.computeMinMax(node.left)
        self.computeMinMax(node.right)
        self.minMax[node] = [node.val, node.val]
        if node.left:
            self.minMax[node][0] = min(self.minMax[node.left][0], node.val)
        if node.right:
            self.minMax[node][1] = max(self.minMax[node.right][1], node.val)

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not self.minMax:
            self.computeMinMax(root)
        if not root:
            return None
        if root.val == key:
            if root.right:
                minFromRight = self.minMax[root.right][0]
                newRoot = TreeNode(minFromRight)
                newRoot.right = self.deleteNode(root.right, minFromRight)
                newRoot.left = root.left
                return newRoot 
            elif root.left:
                maxFromLeft = self.minMax[root.left][1]
                newRoot = TreeNode(maxFromLeft)
                newRoot.left = self.deleteNode(root.left, maxFromLeft)
                newRoot.right = root.right
                return newRoot
            else:
                return None
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            root.left = self.deleteNode(root.left, key)
        return root

