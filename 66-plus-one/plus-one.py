class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # a = ''
        # for i in digits:
        #     a += str(i)
        
        # a = int(a) + 1
        # return list(map(int, list(str(a))))

        for i in range(len(digits) - 1, -1, -1):
                # If the digit is less than 9, just increment and return
                if digits[i] < 9:
                    digits[i] += 1
                    return digits
                # If the digit is 9, set it to 0 and continue the loop
                digits[i] = 0
            
            # If all digits were 9, we need to add a new digit at the beginning
        return [1] + digits