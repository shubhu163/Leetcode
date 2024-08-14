class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # My Solution
        # n = s.strip().replace(' ','').lower()
        # for d in n:
        #     if ord(d) not in range(97,123) and ord(d) not in range(48,58):
        #         n = n.replace(d,'')
        # b = n
        # if n == b[::-1]:
        #     return True

        # return False
        n = ''
        for c in s:
            if c.isalnum():
                n+=c.lower()
        return n == n[::-1]
