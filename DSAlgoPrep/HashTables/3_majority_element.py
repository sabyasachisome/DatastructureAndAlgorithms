"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Input: nums = [3,2,3]
Output: 3
"""
from typing import List
from collections import defaultdict

class Solution:
    def majority_element(self, nums: List[int])->int:
        hash_dict= {}
        arr_len= len(nums)
        for idx in range(arr_len):
            hash_dict[nums[idx]]= hash_dict.get(nums[idx],0)+1
        print(hash_dict)
        for key in hash_dict:
            if hash_dict[key]>= arr_len//2:
                return key
        return -1

    def majorityElementSingleLoop(self, nums: List[int]) -> int:
        elem_dict=defaultdict(int)
        majority_elem_dict={}
        majority_size= len(nums)//2
        for idx in range(len(nums)):
            elem_dict[nums[idx]] += 1
            if elem_dict.get(nums[idx])>majority_size:
                majority_elem_dict[nums[idx]]=elem_dict.get(nums[idx])
                max_item= max(majority_elem_dict)
        return max_item

sol= Solution()
print(sol.majority_element([1,2,3,4,4,4]))