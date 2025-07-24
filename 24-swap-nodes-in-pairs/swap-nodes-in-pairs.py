# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # temp = head
        # p1 = temp

        # while temp.next:
        #     temp = temp.next
        #     p1.next = temp.next
        #     temp.next = p1
        #     p1 = p1.next

        # return head
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        dummy2 = dummy
        slow = head
        fast = head.next

        while fast:
            temp = fast.next
            dummy2.next = fast
            fast.next = slow 
            slow.next = temp

            dummy2 = slow
            slow = temp
            if slow:
                fast = slow.next
            else:
                break

        return dummy.next
