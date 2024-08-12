class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        top = 0
        btm = len(numbers) - 1

        while top!=btm:
                if numbers[top] + numbers[btm] > target:
                        btm -= 1
                elif numbers[top] + numbers[btm] == target:
                    return top+1,btm+1
                else:
                        top += 1
        return []