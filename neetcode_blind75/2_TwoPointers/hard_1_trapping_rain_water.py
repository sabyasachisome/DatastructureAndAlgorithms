"""
42. Trapping Rain Water
Hard
company
Amazon
Goldman Sachs
Adobe
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9
 
Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""
from typing import List

class Solution:
    def trap(self, height: List[int])-> int:
        left_max_height=[]
        right_max_height=[]
        max_height_arr=[]
        for idx in range(len(height)):
            if idx==0:
                left_max_height.append(0)
            else:
                left_max_height.append(max(height[:idx]))
        print(left_max_height)
        for idx in range(len(height)):
            if idx==len(height)-1: 
                right_max_height.append(0)
            else:
                right_max_height.append(max(height[idx+1:]))
        print(right_max_height)
        for idx in range(len(height)):
            if min(left_max_height[idx], right_max_height[idx])- height[idx]<0:
                max_height_arr.append(0)
            else:
                max_height_arr.append(min(left_max_height[idx], right_max_height[idx])- height[idx])
        return sum(max_height_arr)

sol = Solution()
print(sol.trap([4,2,0,3,2,5]))