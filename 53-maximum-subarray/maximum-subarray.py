class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        max_sub = nums[0]
        curr = 0

        for i in nums:
                if curr < 0:
                        curr = 0
                curr += i
                max_sub = max(curr,max_sub)
        return max_sub
        