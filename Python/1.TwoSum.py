# https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Create a dictionary to store the indices of elements
        num_indices = {}
        
        # Iterate through the list
        for i, num in enumerate(nums):
            # Check if the complement of the current number exists in the dictionary
            complement = target - num
            if complement in num_indices:
                # If found, return the indices
                return [num_indices[complement], i]
            # Otherwise, add the current number and its index to the dictionary
            num_indices[num] = i
        
        # If no solution is found
        return []
