from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #Old Approach
        # n = len(nums)
        # cts = defaultdict(int)
        # for i in nums:
        #         cts[i] += 1

        # for i in cts:
        #     if cts[i] > n/2:
        #         return i

        # Moores Algorithm 
        res,cts = 0,0
        for n in nums:
            if cts == 0:
                res = n
            cts += (1 if n == res else -1)
        return res

                    