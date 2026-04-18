class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_v = max(nums)
        ind = nums.index(max_v)
        nums.remove(max_v)
        for i in nums:
            if 2*i > max_v:
                return -1
        return ind
test = Solution()
print(test.dominantIndex([4,6,1,0]))

# nums = [3,6,1,0]