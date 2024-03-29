"""
347. Top K Frequent Elements
Medium

Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int)-> List[int]:
        elem_freq_map={}
        final_op=[]
        num=0
        for idx in range(len(nums)):
            if nums[idx] not in elem_freq_map:
                elem_freq_map[nums[idx]]=1
            else:
                elem_freq_map[nums[idx]]+=1
        sorted_map= {k:v for k,v in sorted(elem_freq_map.items(), key=lambda x:x[1], reverse= True)}
        for key in sorted_map:
            if num<k:
                final_op.append(key)
                num+=1
        return final_op

    def topKFrequent1(self, nums: List[int], k: int)-> List[int]:
        freq_map={}
        all_elem_list=[[] for _ in range(len(nums)+1)]
        for idx in range(len(nums)):
            if nums[idx] not in freq_map:
                freq_map[nums[idx]]=1
            else:
                freq_map[nums[idx]]+=1
        
        for key,val in freq_map.items():
            all_elem_list[val].append(key)
        final_arr_list=[]
        for idx in range(len(all_elem_list)-1,-1,-1):
            for item in all_elem_list[idx]:
                final_arr_list.append(item)
            if len(final_arr_list)==k:
                return final_arr_list

sol= Solution()
print(sol.topKFrequent1([1,1,1,2,2,3], 2))