# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1,p2 = list1,list2
        dummy = ListNode(-1)
        curr = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                temp = p1.next
                curr.next = p1
                p1 = temp
            else:
                temp = p2.next
                curr.next = p2
                p2 = temp
            curr = curr.next
        if p1:
            curr.next = p1
        if p2:
            curr.next= p2
        
        return dummy.next



        