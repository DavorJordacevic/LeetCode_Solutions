# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False
        
        '''
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                for r in row:
                    if r == target:
                        return True
        return False
        '''

        rows, cols = len(matrix), len(matrix[0])
        left = 0
        right = rows*cols-1

        while left <= right:
            mid = (left + right) // 2
            mid_element = matrix[mid//cols][mid % cols]

            if mid_element == target:
                return True
            elif mid_element < target:
                left = mid + 1
            else:
                right = mid - 1

        return False