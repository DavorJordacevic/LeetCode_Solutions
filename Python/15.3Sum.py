# https://leetcode.com/problems/3sum/description/

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        
        sorted_nums = sorted(nums)

        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            target = -sorted_nums[i]

            l = i + 1
            r = len(sorted_nums) - 1

            while l < r:
                if sorted_nums[l] + sorted_nums[r] == target:
                    results.append([sorted_nums[i], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    while l < r and sorted_nums[l] == sorted_nums[l-1]:
                        l += 1
                elif sorted_nums[l]+sorted_nums[r] < target:
                    l += 1
                else:
                    r -= 1
        return results