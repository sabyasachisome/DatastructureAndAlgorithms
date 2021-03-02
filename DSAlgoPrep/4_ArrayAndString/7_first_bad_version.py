# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):
"""
This program is for compiling purpose, not for running
"""

class Solution:
    def isBadVersion(self, version):
        pass

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start=1
        end= n
        while(start<end):
            mid= (start+end)//2
            if not self.isBadVersion(mid):
                start=mid+1
            else:
                end=mid
        return start
