"""
Given an unsorted array Arr of size N. Find the subarray Arr[s...e] such that
sorting this subarray makes the whole array sorted.

Example 1:

Input:
N = 11
Arr[] ={10,12,20,30,25,40,32,31,35,50,60}
Output: 3 8
Explanation: Subarray starting from index
3 and ending at index 8 is required
subarray. Initial array: 10 12 20 30 25
40 32 31 35 50 60 Final array: 10 12 20
25 30 31 32 35 40 50 60
(After sorting the bold part)

Example 2:

Input:
N = 9
Arr[] = {0, 1, 15, 25, 6, 7, 30, 40, 50}
Output: 2 5
Explanation: Subarray starting from index
2 and ending at index 5 is required
subarray.
Initial array: 0 1 15 25 6 7 30 40 50
Final array:   0 1 6 7 15 25 30 40 50
(After sorting the bold part)
"""
# from collections import defaultdict
# from typing import List
class Solution:

	def printUnsorted(self, arr, n):
		arr_index_map= {}
		for idx in range(len(arr)):
			arr_index_map[arr[idx]]= idx
		sorted_arr_index_map= {k:v for k, v in sorted(arr_index_map.items(), key= lambda item: item[0])}
		sorted_arr_index_list= list(sorted_arr_index_map.values())
		start=0
		for idx in range(len(sorted_arr_index_list)-1):
			if sorted_arr_index_list[idx+1]-sorted_arr_index_list[idx]!=1:
				start= idx+1
				break
		end=0
		for idx in range(start, len(sorted_arr_index_list)-1):
			if sorted_arr_index_list[idx+1]-sorted_arr_index_list[idx]==1:
				end= idx-1
		return start, end

sol= Solution()
arr=[10,12,20,30,25,40,32,31,35,50,60]
arr1=[1,468,335,170,225,479,359,463,465,206,146,282,328,462,492,496,443,328,437,392,105,403,154,293,383,422,217,219,396,448,227,272,39,370,413,168,300,36,395,204,312,323]
print(sol.printUnsorted(arr1, len(arr1)))