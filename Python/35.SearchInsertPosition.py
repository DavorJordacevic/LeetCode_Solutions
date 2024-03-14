# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.
# https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #nums.append(target)
        #nums = list(sorted(set(nums)))
        #return nums.index(target)

        low = 0
        high = len(nums) - 1

        while low <= high:
            n = (low + high) // 2
            if nums[n] == target:
                return n
            elif nums[n] > target:
                high = n - 1
            elif nums[n] < target:
                low = n + 1
        return low
