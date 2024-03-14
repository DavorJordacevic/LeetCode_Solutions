// Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
// You must write an algorithm with O(log n) runtime complexity.
// https://leetcode.com/problems/search-insert-position/description/

#include <iostream>
#include <vector>

class Solution {
public:
    int searchInsert(vector<int>& nums, int target){
        int low = 0;
        int high = nums.size() - 1;
        
        while (low <= high) {
            int n = (low+high) / 2;
            
            if (nums[n] == target){
                return n;
            }
            else if (nums[n] > target){
                high = n - 1;
            } else {
                low = n + 1;
            }
        }
        return low;
        
    }    
};
