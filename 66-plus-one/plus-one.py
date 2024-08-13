class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = ''
        for i in digits:
            a += str(i)
        
        a = int(a) + 1
        return list(map(int, list(str(a))))

