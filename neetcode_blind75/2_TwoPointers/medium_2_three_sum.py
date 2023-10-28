"""
15. 3Sum
Medium
28.9K
2.6K
company
Facebook
company
Amazon
company
Adobe
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""
from typing import List
class Solution:
    def threeSum(self, nums: List[int])-> List[List[int]]:
        nums.sort()
        print(nums)
        target_sum=0
        final_arr=[]
        for idx, elem in enumerate(nums):
            if idx>0 and elem==nums[idx-1]:
                continue
            left= idx+1
            right= len(nums)-1
            # print(idx, left, right)
            while left<right:
                three_sum= elem+nums[left]+nums[right]
                if three_sum< target_sum:
                    left+=1
                elif three_sum> target_sum:
                    right-=1
                    # print(idx, left, right)
                else:
                    final_arr.append([elem, nums[left], nums[right]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return final_arr

sol= Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))