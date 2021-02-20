from typing import List

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

sol= Solution()
print(sol.majority_element([1,2,3,4,4,4]))