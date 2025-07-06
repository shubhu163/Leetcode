class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # prefix = [1] * len(nums)
        # suffix = [1] * len(nums)
        # tot = 1

        # for i in range(len(nums)):
        #     tot = 1 if i == 0 else prefix[i-1] * nums[i-1]
        #     prefix[i] = tot

        # nums2 = nums[::-1]
        # for i in range(len(nums2)):
        #     tot = 1 if i == 0 else suffix[i-1] * nums2[i-1]
        #     suffix[i] = tot
        
        # suffix.reverse()
        # for i in range(len(nums)):            
        #     nums[i] = suffix[i] * prefix[i]
        # return nums

        nums2 = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            nums2[i] = prefix
            prefix = prefix * nums[i]

        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            nums2[i] = nums2[i] * postfix
            postfix = postfix * nums[i]

        return nums2





        

        


        
        