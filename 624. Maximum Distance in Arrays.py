class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        min_v = 10000
        max_v = -10000
        res = 0
        for arr in arrays:
            res = max(res,arr[-1] - min_v, max_v- arr[0])
            min_v = min(min_v, arr[0])
            max_v = max(max_v, arr[-1])
        return res

arrays =    [[1,5],[3,4]]
print(Solution().maxDistance(arrays))