# https://leetcode.com/problems/climbing-stairs/description/

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        
        comb = [0] * (n + 1)
        comb[1] = 1
        comb[2] = 2
        
        for i in range(3, n + 1):
            comb[i] = comb[i - 1] + comb[i - 2]
        return comb[n]
