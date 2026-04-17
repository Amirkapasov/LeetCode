class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        count = 0
        for i in nums:
            if i == 1:
                count += 1
            elif i == 0:
                res.append(count)
                count = 0
        res.append(count)
        return max(res)

test = Solution()
print(test.findMaxConsecutiveOnes([1,1,0,1,1,1]))
