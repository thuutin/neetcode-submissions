# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        res = []
        while l1 != None or l2 != None:
            if l1 != None:
                a = l1.val
                l1 = l1.next
            else:
                a = 0
            if l2 != None:
                b = l2.val
                l2 = l2.next
            else:
                b = 0
            if a + b + carry < 10:
                res.append(a + b + carry)
                carry = 0
            else:
                res.append(a + b + carry - 10)
                carry = 1
                
        if carry == 1:
            res.append(1)
        #print(res)
        prev = None

        for i in range(len(res) - 1, -1, -1):
            node = ListNode()
            node.next = prev
            node.val = res[i]
            prev = node
        return prev