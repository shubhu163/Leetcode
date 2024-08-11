class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # My solution - return True if sorted(list(s)) == sorted(list(t)) else False 

        # Neetcode Solution  - 
        if len(s) != len(t):
            return False
        c_T,c_S = {},{}
        for i in range(len(s)):
            c_S[s[i]] = 1 + c_S.get(s[i],0)
            c_T[t[i]] = 1 + c_T.get(t[i],0)
        for c in c_S:
            if c_S[c] != c_T.get(c,0):
                return False

        return True

        

