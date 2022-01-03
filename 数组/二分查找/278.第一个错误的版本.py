# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start < end:
            # 结束条件是start == end
            mid = start + (end - start) // 2
            if isBadVersion(mid):
                # 在mid之前就存在Bad Version
                end = mid
            else:
                # Bad Version在mid之后
                start = mid + 1
        return start