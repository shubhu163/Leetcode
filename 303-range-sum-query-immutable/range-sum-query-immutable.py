class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.prefixsum = []
        total = 0
        for n in nums:
            total += n
            self.prefixsum.append(total)
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sumright = self.prefixsum[right]
        subleft = self.prefixsum[left-1] if left > 0 else 0
        return sumright - subleft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)