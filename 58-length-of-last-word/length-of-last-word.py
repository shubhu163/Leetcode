class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        remove = '1234567890.,\'!&*?/"'

        i = len(s) - 1
        count = 0

        while i>-1:
            if s[i] in remove:
               i -= 1

            
            if ord(s[i].lower()) >= ord('a') and ord(s[i].lower()) <= ord('z'):
                count+=1
                i -= 1
            
            else:       
                break
        
        return count



        