# https://leetcode.com/problems/power-of-two/

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        if n > 0:
            # n is positive
            if n == 1:
                # 2 ^ 0
                return True
            else:
                # n is 2 or more.
                while n != 2:
                    if n % 2 == 1:
                        # n is now odd, so can't be further divided by 2
                        return False
                    else:
                        n = n/2
                # n kept dividing by 2, so it is a power of 2
                return True
        else:
            # n is negative, or 0, so it is not a power of 2
            return False