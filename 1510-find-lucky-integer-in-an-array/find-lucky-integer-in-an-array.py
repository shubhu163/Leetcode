from collections import defaultdict
class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = defaultdict(int)
        for n in arr:
            count[n] += 1
        
        l = []
        for n in count:
            if n == count[n]:
                l.append(n)

        return max(l) if l else -1       



    
        