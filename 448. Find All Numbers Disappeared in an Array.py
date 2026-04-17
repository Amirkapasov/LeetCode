class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        maximum = len(nums)
        must_be = set([i for i in range(1,maximum+1)])
        nums = set(nums)
        res = must_be.difference(nums)
        return list(res)