import math
class Solution(object):
    def __init__(self):
        self.last_n = 2
        self.prime_nums = []

    def is_prime(self, p):
        k = 2

        # if k < n and rem is 0 print (n, "is not prime, since it divides by ", k) else k = k + 1

        # Optimization: Check only till sqrt(n): https://www.themathdoctors.org/prime-numbers-checking-one-part-1/#:~:text=One%20method%20entails%20dividing%20the%20number%20by%20every,all%20the%20primes%20less%20than%20its%20square%20root.
        while k < math.sqrt(p):
            if p % k == 0:
                return False
            else:
                k = k + 1

        return True

    def count_in_prime_nums(self, n):
        # Count number of primes smaller than n in self.prime_nums
        i = 0
        sz = len(self.prime_nums)

        while self.prime_nums[i] < n and i < sz:
            i = i + 1

        return i


    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        if n < self.last_n:
            return self.count_in_prime_nums(n)

        # Now n >= 3
        
        i = self.last_n
        while i < n:
            if self.is_prime(p = i): 
                self.prime_nums.append(i)                               
            i = i + 1
        
        self.last_n = n

        return len(self.prime_nums)

sol = Solution()
inputs = [10, 5, 25, 7, 9, 96, 45, 10235, 8767, 499979]

for ip in inputs:
    print(ip, sol.countPrimes(ip))

