class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)

        right = 0
        for i in range(len(nums)-1, -1,-1):
            postfix[i] = right
            right = right + nums[i]

        left = 0
        for i in range(len(nums)):
            prefix[i] = left
            left = left + nums[i]
            if prefix[i] == postfix[i]:
                return i
        

        return -1


