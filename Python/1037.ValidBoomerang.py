# https://leetcode.com/problems/valid-boomerang/description/

class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        
        area = 0.5 * (points[0][0]*points[1][1] - points[0][0]*points[2][1] + points[1][0]*points[2][1] - points[1][0]*points[0][1] + points[2][0]*points[0][1] - points[2][0]*points[1][1])
        return area != 0