# https://leetcode.com/problems/k-closest-points-to-origin/

import math
import numpy as np

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        distances = []

        for p in points:
            distances.append((p, self.distance(p)))

        distances.sort(key=lambda x: x[1])
        return [p[0] for p in distances[:k]]

    def distance(self, p):
        return math.sqrt(p[0]**2 + p[1]**2)