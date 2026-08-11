# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        prev = None
        while list1 or list2:
            if not list1 or (list2 and list1.val > list2.val):
                selected = list2
                list2 = list2.next    
            else:
                selected = list1
                list1 = list1.next
            if prev:
                prev.next = selected
            prev = selected
            if not head:
                head = prev
        return head