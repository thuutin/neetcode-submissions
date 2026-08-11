# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        def reverse(node):
            prev = None
            while node != None:
                print(node.val)
                nex = node.next
                node.next = prev
                prev, node = node, nex
            return prev
            
        l1 = head
        l2 = reverse(mid)
        def ppp(n):
            r = []
            while n:
                r.append(n.val)
                n = n.next
            print(r)
        ppp(l1)
        ppp(l2)
        while l1 and l2:
            l1n = l1.next
            l2n = l2.next
            l1.next, l2.next = l2, l1.next
            l1, l2 = l1n, l2n
        return None