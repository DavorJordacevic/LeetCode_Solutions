# https://leetcode.com/problems/median-of-two-sorted-arrays/description/

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums = sorted(nums1 + nums2)
        mid = len(nums) // 2
        return (nums[mid] + nums[~mid] / 2.0)