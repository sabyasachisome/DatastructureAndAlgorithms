"""
Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.
The result is going to be very large, hence return the result in the form of a string.

Example 1:

Input:
N = 5
Arr[] = {3, 30, 34, 5, 9}
Output: 9534330
Explanation: Given numbers are {3, 30, 34,
5, 9}, the arrangement 9534330 gives the
largest value.

Your Task:
You don't need to read input or print anything. Your task is to complete the function printLargest()
which takes the array of strings arr[] as parameter and returns a string denoting the answer.

Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(1)

Constraints:
1 ≤ N ≤ 105
0 ≤ Arr[i] ≤ 1018
"""

#User function Template for python3
from collections import defaultdict
from typing import List
from itertools import permutations
class Solution:

    def printLargest(self,arr):
        all_nums= [int(''.join(map(str,list_item))) for list_item in list(permutations(arr, len(arr)))]
        all_nums.sort(reverse=True)
        return all_nums[0]

    def merge(self, left: List[int], right: List[int])-> str:
        i=0
        j=0
        res=[]
        # print(type(left),type(left))
        while(i< len(left) and j<len(right)):
            if int(left[i]+right[j])>int(right[j]+left[i]):
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        while(i<len(left)):
            res.append(left[i])
            i+=1
        while(j<len(right)):
            res.append(right[j])
            j+=1
        return res

    def merge_sort(self, arr):
        if len(arr) <=1:
            return arr
        mid= len(arr)//2
        left= self.merge_sort(arr[:mid])
        right= self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def largest_number(self, arr: List[int]) -> str:
        largest_num= self.merge_sort(arr)
        return largest_num

if __name__ == '__main__':
    tc= int(input())
    while(tc>0):
        n= int(input())
        # arr = [3, 30, 34, 5, 9]
        arr= list(map(str, input().strip().split()))
        ob= Solution()
        ans= ob.merge_sort(arr)
        print(''.join(map(str,ans)))
        tc-=1