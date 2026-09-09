# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l = []
        node = head
        while node != None:
            l.append(node)
            node = node.next
        res = []
        i = 0
        j = len(l) - 1
        while i <= j:
            if i < j:
                res.append(l[i])
                res.append(l[j])
            else:
                res.append(l[i])
            i += 1
            j -= 1
        #print(list(map(lambda x: x.val, res)))
        for i in range(len(res)):
            res[i].next = None
            if i + 1 < len(res):
                res[i].next = res[i + 1]
        


