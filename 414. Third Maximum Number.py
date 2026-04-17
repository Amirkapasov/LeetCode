class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) < 3:
            return max(nums)
        for i in range(2):
            a = max(nums)
            for i in range(nums.count(a)):
                nums.remove(a)
        return max(nums)

test = Solution()
print(test.thirdMax([3,2,1]))