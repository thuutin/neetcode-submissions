# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = {}
        def dfs(node, index):
            if node:
                res[index] = node.val
                if node.left:
                    dfs(node.left, index * 2 + 1)
                if node.right:
                    dfs(node.right, index * 2 + 2)
        dfs(root, 0)
        return ",".join(map(lambda item: str(item[0]) + ':' + str(item[1]) , res.items()))

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = {}
        if not data:
            return None
        for item in data.split(","):
            k, v = item.split(":")
            arr[int(k)] = int(v)
        def build_tree(index):
            if index not in arr:
                return None
            node = TreeNode(arr[index])
            left = index * 2 + 1
            right = left + 1
            node.left = build_tree(left)
            node.right = build_tree(right)
            return node
        
        if not arr or not arr[0]:
            return None
        return build_tree(0)
        