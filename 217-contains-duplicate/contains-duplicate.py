class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        used = set()
        for i in nums:
            if i not in used:
                used.add(i)
            else:
                return True
        return False
        