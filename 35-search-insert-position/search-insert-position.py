class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        diff = []
        if target > nums[len(nums)-1]:
                return len(nums)
        
        elif target < nums[0]:
            return 0
        if target in nums:
            for i in range(len(nums)):
                if nums[i] == target:
                    return i

        else:
            for i in range(len(nums)):
                print('I')
                d = target - nums[i] if target - nums[i] > 0 else  float('inf')
                if d <  float('inf'):
                    diff.append((d,i))
            print(diff)
            return min(diff)[1] + 1


