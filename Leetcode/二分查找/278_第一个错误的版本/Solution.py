# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if isBadVersion(1):
            return 1
        start, end = 1, n
        while start+1 < end:
            mid = (start+end)//2
            if isBadVersion(mid) and not isBadVersion(mid-1):
                return mid
            elif isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start) and not isBadVersion(start-1):
            return start
        if isBadVersion(end) and not isBadVersion(end-1):
            return end