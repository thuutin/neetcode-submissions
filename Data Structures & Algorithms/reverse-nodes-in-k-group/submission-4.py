# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next
        
        newNodes = []
        for i in range(len(nodes) // k + 1):
            knodes = nodes[i * k:(i + 1) * k]
            if len(knodes) == k:
                newNodes.extend(knodes[::-1])
            else:
                newNodes.extend(knodes)
        #print(list(map(lambda x: x.val, newNodes)))
        for i in range(len(newNodes)):
            if i + 1 < len(newNodes):
                newNodes[i].next = newNodes[i + 1]
            else:
                newNodes[i].next = None
        return newNodes[0]
