class Solution(object):
    def checkPossibility(self, nums):
        count = 0
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                if count == 1:
                    return False
                count += 1
                if i == 1 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return True

test = Solution()
print(test.checkPossibility([4,2,1]))
