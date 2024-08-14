class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # My Solution
        n = s.strip().replace(' ','').lower()
        for d in n:
            if ord(d) not in range(97,123) and ord(d) not in range(48,58):
                n = n.replace(d,'')

        b = ''
        for i in range(len(n)-1,-1,-1):
            b +=n[i]
        if b == n:
            return True

        return False