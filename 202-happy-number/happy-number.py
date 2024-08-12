class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        num = n
        seen_numbers = set()

        def sumj(n):
            n_list = list(str(n))
            sum = 0
            for i in n_list:
                sum += int(i) * int(i)
            if sum == 1:
                return True
            elif sum in seen_numbers:
                return False
            else:
                seen_numbers.add(sum)
                return sumj(sum)

        return sumj(n)