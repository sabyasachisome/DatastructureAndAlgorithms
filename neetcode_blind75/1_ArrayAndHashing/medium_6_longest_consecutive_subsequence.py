"""
128. Longest Consecutive Sequence
Medium
company
Amazon
Google
Adobe
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int])-> int:
        elem_set= set(nums)
        i=0
        max_subset_len=0
        while i<len(nums):
            start= nums[i]
            if start-1 not in elem_set:
                subset_len=1
                while start+1 in elem_set:
                    subset_len+=1
                    max_subset_len= max(max_subset_len, subset_len)
                    start+=1
            i+=1
        return max_subset_len

sol= Solution()
print(sol.longestConsecutive([100,4,200,1,3,2]))