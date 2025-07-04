# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0,head)
        first = dummy
        second = head

        while n>0 and second:
            second = second.next
            n -= 1
        
        while second:
            first = first.next
            second = second.next

        first.next = first.next.next

        return dummy.next



