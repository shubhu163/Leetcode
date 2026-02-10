class Solution(object):
    def longestBalanced(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        out  = 0

        for i in range(0,n):
            even = set()
            odd = set()
            for j in range(i,n):
                if nums[j] %2  == 0:
                    even.add(nums[j])
                else:
                    odd.add(nums[j])
                
                if len(even) == len(odd):
                    out = max(out, j-i + 1)
        
        return out













        