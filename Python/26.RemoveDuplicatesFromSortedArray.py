# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        l = 0
        for i in range(len(nums)):
            if nums[i] != nums[l]:
                l+=1
                nums[l] = nums[i]
                
        return l+1