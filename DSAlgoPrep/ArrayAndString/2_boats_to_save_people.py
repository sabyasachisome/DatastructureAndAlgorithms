"""
You are given an array people where people[i] is the weight of the ith person,
and an infinite number of boats where each boat can carry a maximum weight of limit.
Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
"""

from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int)-> int:
        i=0
        j=len(people)-1
        no_of_boats=0
        sorted_people= sorted(people)
        while(i<=j):
            if (i==j):
                no_of_boats+=1
                break
            if sorted_people[i]+sorted_people[j]<=limit:
                i+=1

            no_of_boats += 1
            j-=1
        return no_of_boats

people = [1,2]
limit = 3
sol= Solution()
print(sol.numRescueBoats(people, limit))
