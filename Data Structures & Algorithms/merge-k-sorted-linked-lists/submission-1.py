# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush( heap, (l.val, i))
        head = None
        prev = None
        while heap:
            top, i = heapq.heappop(heap)
            if prev:
                prev.next = lists[i]
            if not head:
                head = prev
            prev = lists[i]
            lists[i] = lists[i].next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
        return head
