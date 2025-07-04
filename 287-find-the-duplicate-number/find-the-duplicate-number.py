class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i,j = 0,1
        while j<len(nums):
            if nums[i] == nums[j]:
                return nums[i]
            i += 1
            j += 1
        

        