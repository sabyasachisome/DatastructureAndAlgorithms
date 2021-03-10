"""
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight,
so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even).
Alice likes her candies very much, and she wants to eat the maximum number of different types of candies
while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she
can eat if she only eats n / 2 of them.

Input: candyType = [1,1,2,2,3,3]
Output: 3
Explanation: Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type.

Input: candyType = [6,6,6,6]
Output: 1
Explanation: Alice can only eat 4 / 2 = 2 candies. Even though she can eat 2 candies, she only has 1 type.

Constraints:
n == candyType.length
2 <= n <= 104
n is even.
-105 <= candyType[i] <= 105
"""

from typing import List

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        max_candies_to_eat= len(candyType)//2
        candy_freq_map={}
        for idx in range(len(candyType)):
            if candy_freq_map.get(candyType[idx],0)==0:
                candy_freq_map[candyType[idx]]=1
            else:
                candy_freq_map[candyType[idx]]+=1
        max_candy_in_option= len(candy_freq_map.keys())
        return min(max_candies_to_eat, max_candy_in_option)

sol= Solution()
print(sol.distributeCandies([1,1,2,2,3,3]))