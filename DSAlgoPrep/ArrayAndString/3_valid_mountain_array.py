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