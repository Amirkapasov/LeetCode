class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        total = []
        if len(nums) == k:
            return sum(nums) / k
        while len(nums) != k:
            dobav = sum(nums[:k])
            nums.pop(0)
            total.append(dobav)
        else:
            return float(max(total) / k)

test = Solution()
print(test.findMaxAverage(nums = [4,0,4,3,3], k = 5))