from typing import List

class Solution:
    def two_sum(self, A:List[int], B: List[int], C:List[int], D:List[int]) -> List[int]:
        hash_map= {}
        for i in range(len(A)):
            x=A[i]
            for j in range(len(B)):
                y=B[j]
                sum_pair= x+y
                if sum_pair not in hash_map:
                    hash_map[sum_pair]=0

                hash_map[sum_pair]+=1

        ans=0
        for i in range(len(C)):
            x = C[i]
            for j in range(len(D)):
                y= D[j]
                check_sum= x+y
                if check_sum in hash_map:
                    ans+=hash_map[check_sum]
        return ans
sol= Solution()
print(sol.two_sum([1,-1],[-1,-1],[-2,2],[2,-2]))
