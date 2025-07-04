class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower().replace(' ','')
        for d in s:
            if ord(d) not in range(97,123) and ord(d) not in range(48,58):
                s = s.replace(d,'')
        
        l,r = 0, len(s)-1
        while l<r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
