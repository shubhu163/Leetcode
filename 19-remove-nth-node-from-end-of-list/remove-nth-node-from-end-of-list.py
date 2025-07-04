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
        if not head or not head.next:
            return None
        dummy = ListNode(0,head)
        first = head
        second = head
        i = n

        while i>0 and second:
            second = second.next
            i -= 1

        while not second:
            dummy.next = head.next
            return dummy.next
                
        while second.next:
            first = first.next
            second = second.next
        
        tmp = first.next
        first.next = tmp.next

        return dummy.next


