# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = 1
        node = head
        while node.next != None:
            l += 1
            node = node.next
        n = l - n
        prev = None
        toRemove = head
        if n == 0 and l == 1:
            return None
        print(n, l)
        i = 0
        while i < n:
            if toRemove.next == None:
                return head
            prev = toRemove
            toRemove = toRemove.next
            i += 1
        if prev == None:
            return toRemove.next
        prev.next = toRemove.next
        return head
        