class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        cts = {}
        for i,n in enumerate(nums):
                diff = target - n
                if diff in cts:
                        return cts[diff],i
                cts[n] = i
                

        