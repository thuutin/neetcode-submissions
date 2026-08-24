# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        knodes = []
        node = head
        i = 0
        while i < k and node:
            knodes.append(node)
            node = node.next
            i += 1
        if len(knodes) < k:
            return head
        for i in range(1, len(knodes)):
            knodes[i].next = knodes[i - 1]
        knodes[0].next = self.reverseKGroup(node, k)
        return knodes[-1]