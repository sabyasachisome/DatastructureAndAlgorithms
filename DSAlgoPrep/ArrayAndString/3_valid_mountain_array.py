"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

from typing import List

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i: int=1
        arr_len= len(arr)
        while (i< arr_len and arr[i]>arr[i-1]):
            i+=1
        if i==1 or i==arr_len:
            return False
        while (i< arr_len and arr[i]<arr[i-1]):
            i+=1
        return i==arr_len

arr=[0,3,2,1]
sol= Solution()
print(sol.validMountainArray(arr))