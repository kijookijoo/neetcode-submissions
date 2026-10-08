# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return 
        def merge(l1, l2):
            dummy = ListNode(-1)
            curr = dummy
            p1, p2 = l1, l2
            while p1 and p2:
                if p1.val <= p2.val:
                    curr.next = p1
                    p1 = p1.next
                else:
                    curr.next = p2
                    p2 = p2.next
                curr = curr.next
            if p1:
                curr.next = p1
            if p2:
                curr.next = p2
            return dummy.next
        
        while len(lists) >= 2:
            merged = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged.append(merge(l1, l2))
            lists = merged
        
        return lists[0]
        