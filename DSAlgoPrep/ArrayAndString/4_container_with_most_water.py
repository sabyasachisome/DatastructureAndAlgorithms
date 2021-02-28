"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0).
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Notice that you may not slant the container.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        max_area=0
        while(left<right):
            max_area= max(max_area,(min(height[left],height[right])*(right-left)))
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_area

sol= Solution()
print(sol.maxArea([1,8,6,2,5,4,8,3,7]))