# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        values = []
        node = head
        while node != None:
            print(node.val)
            values.append(node.val)
            node = node.next
        
        i = len(values) - 1
        j = 0
        while j<i:
            if values[j] != values[i]:
                return False
            i -= 1
            j += 1
        return True

        # while i>=0:
        #     if head.val != values[i]:
        #         return False
        #     head = head.next
        #     i-=1
        # return True

        
