from typing import List
from collections import defaultdict

class Solution:
    def check_duplicate(self, nums: List[int]) -> bool:
        dictt= defaultdict(int)
        for idx in range(len(nums)):
            if dictt[nums[idx]]:
                return True
            dictt[nums[idx]]+=1
        return False

sol= Solution()
print(sol.check_duplicate([1,2,3,4,5,5]))