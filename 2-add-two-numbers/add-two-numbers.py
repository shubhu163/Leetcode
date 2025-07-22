# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        list1 = []
        list2 = []
        cur1, cur2 = l1, l2

        while cur1:
            list1.append(cur1.val)
            cur1 = cur1.next

        while cur2:
            list2.append(cur2.val)
            cur2 = cur2.next

        print(list1, list2)

        if len(list1) >= len(list2):
            dummy = ListNode(0, l1)
            l = l1
        else:
            dummy = ListNode(0, l2)
            l = l2

        carry = 0
        while l1 or l2:
            if l1 and l2:
                temp = l1.val + l2.val + carry
                l.val = temp % 10
                carry = temp // 10
                l1 = l1.next
                l2 = l2.next
                l = l.next
            else:
                temp = l.val + carry
                l.val = temp % 10
                carry = temp // 10
                l = l.next
                if l1: l1 = l1.next
                if l2: l2 = l2.next

        # ✅ Handle carry at the end if it's still > 0
        if carry:
            # Move to the end of the list
            tail = dummy
            while tail.next:
                tail = tail.next
            tail.next = ListNode(carry)

        return dummy.next
