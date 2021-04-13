"""
Given a non-negative number represented as a list of digits, add 1 to the number (increment the number represented by the digits).
The digits are stored such that the most significant digit is first element of array.

Example 1:

Input:
N = 3
arr[] = {1, 2, 4}
Output:
1 2 5
Explanation:
124+1 = 125, and so the Output

Example 2:

Input:
N = 3
arr[] = {9,9,9}
Output:
1 0 0 0
Explanation:
999+1 = 1000, and so the output
"""

class Solution:
    def increment(self, arr, N):
        last_num= arr[-1]
        last_num+=1
        carry= last_num//10
        arr[-1]= last_num%10
        for idx in range(len(arr)-2, -1, -1):
            if carry>0:
                arr[idx]+=carry
                carry= arr[idx]//10
                arr[idx]= arr[idx]%10
        if carry>0:
            arr.insert(0, carry)
        return arr

if __name__ == '__main__':
    t= int(input())
    for _ in range(t):
        N= int(input())
        arr= list(map(int, input().split()))

        ob= Solution()
        ptr= ob.increment(arr, N)
        for i in ptr:
            print(i, end= "")
        print()

