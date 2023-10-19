# Problem: https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits[-1] < 9 :
            digits[-1] += 1
            return digits
        else:
            to_add = 1
            k = -1
            min_k = -1 * len(digits)
            while to_add == 1 :
                sum = digits[k] + to_add
                if sum == 10 :
                    digits[k] = 0
                else:
                    # No more carry for next stage, we're done
                    digits[k] = sum
                    break
                k = k - 1
                # If all digits are 9, we'll need to insert a new digit once we reach beginning of list
                if k < min_k:
                    # Insert the carry as new digit and we're done
                    digits.insert(0, 1)
                    break

            return digits
        
sol = Solution()
print(sol.plusOne([4,3,7]))
print(sol.plusOne([4,3,9]))
print(sol.plusOne([4,9,9]))
print(sol.plusOne([9,9,9]))
print(sol.plusOne([9,9,9,9,9,9,9,9,9,9,9,9,9,9]))