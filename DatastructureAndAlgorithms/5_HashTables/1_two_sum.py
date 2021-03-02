from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        dictt={}
        len_of_arr= len(nums)
        for arr_elem_idx in range(len_of_arr):
            balance= target-nums[arr_elem_idx]
            if balance in dictt:
                return (dictt[balance], arr_elem_idx)
            dictt[nums[arr_elem_idx]]= arr_elem_idx

sol= Solution()
answer= sol.two_sum([1,2,3,4,54,6],8)
print(answer)