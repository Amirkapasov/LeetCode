class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        maxi = max(dict.values())
        for i, j in dict.items():
            if j == maxi:
                return i

test = Solution()
print(test.majorityElement([3,2,3]))