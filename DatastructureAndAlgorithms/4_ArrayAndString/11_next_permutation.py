"""
Implement the next permutation, which rearranges the list of numbers into Lexicographically next greater
permutation of list of numbers. If such arrangement is not possible, it must be rearranged to the lowest
possible order i.e. sorted in an ascending order. You are given an list of numbers arr[ ] of size N.

Example 1:

Input: N = 6
arr = {1, 2, 3, 6, 5, 4}
Output: {1, 2, 4, 3, 5, 6}
Explaination: The next permutation of the
given array is {1, 2, 4, 3, 5, 6}

Example 2:

Input: N = 3
arr = {3, 2, 1}
Output: {1, 2, 3}
Explaination: As arr[] is the last
permutation. So, the next permutation
is the lowest one.
"""

class Solution:
    def nextPermutation(self, N, arr):
        start=N-1
        while(start>0):
            if arr[start]>arr[start-1]:
                break
            start -= 1
        if start==0:
            return sorted(arr)
        check_idx= start-1
        next_greater_elem_subarray= sorted(arr[start:])
        for i in range(len(next_greater_elem_subarray)):
            if next_greater_elem_subarray[i]>arr[check_idx]:
                next_greater_elem_subarray[i], arr[check_idx]= arr[check_idx], next_greater_elem_subarray[i]
                break
        new_arr= arr[:start]+next_greater_elem_subarray
        return new_arr

sol= Solution()
arr= [1, 2, 3, 6, 5, 4]
arr1=[3,2,1]
arr2=[4,5,2,1,3]
arr3=[62, 92, 96, 43, 28, 37, 92, 5, 3, 54, 93, 83, 22]
arr4=[3,2,1,23]
print(sol.nextPermutation(len(arr), arr))