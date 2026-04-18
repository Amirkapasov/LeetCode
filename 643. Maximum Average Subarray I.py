class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr = sum(nums[:k])
        max_sum = curr
        for i in range(k, len(nums)):
            curr += nums[i]-nums[i-k]
            if curr > max_sum:
                max_sum = curr
        return max_sum / float(k)


test = Solution()
print(test.findMaxAverage(nums = [4,0,4,3,3], k = 5))