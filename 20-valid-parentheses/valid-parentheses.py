class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        closed = {
            ')' :'(',
            ']' : '[',
            '}' : '{'
        }
        stack = []

        for i in s:
            if i in closed and stack:
                if closed[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            
            else:
                stack.append(i)   
        return True if not stack  else False       


