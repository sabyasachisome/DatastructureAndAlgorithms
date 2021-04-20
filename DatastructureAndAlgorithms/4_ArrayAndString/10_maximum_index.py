"""
Given an array A[] of N positive integers.
The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].

Example 1:

Input:
N = 2
A[] = {1, 10}
Output:
1
Explanation:
A[0]<=A[1] so (j-i) is 1-0 = 1.

Example 2:

Input:
N = 9
A[] = {34, 8, 10, 3, 2, 80, 30, 33, 1}
Output:
6
Explanation:
In the given array A[1] < A[7]
satisfying the required
condition(A[i] <= A[j]) thus giving
the maximum difference of j - i
which is 6(7-1).

Your Task:
The task is to complete the function maxIndexDiff()
which finds and returns maximum index difference. Printing the output will be handled by driver code.
"""

class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,arr, n):
        # traverse the array:
        #     traverse from last till before current index:
        #         if inner loop is greater than outer loop element and diff in index > max:
        #             max= new diff in index
        max_diff=0
        for i in range(n):
            j=n-1
            while(j>i):
                if arr[i]<arr[j] and j-i>max_diff:
                    max_diff=j-i
                j-=1
        return max_diff

sol= Solution()
arr=[34, 8, 10, 3, 2, 80, 30, 33, 1]
print(sol.maxIndexDiff(arr, len(arr)))