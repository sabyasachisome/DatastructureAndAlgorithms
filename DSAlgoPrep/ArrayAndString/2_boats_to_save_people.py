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
                no_of_boats += 1
                i+=1
                j-=1
            else:
                no_of_boats += 1
                j-=1
        return no_of_boats

people = [1,2]
limit = 3
sol= Solution()
print(sol.numRescueBoats(people, limit))
