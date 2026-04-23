class Solution(object):
    def rotateString(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        str = s+s
        len_goal = len(goal)
        for i in range(len_goal):
            if goal == str[i:len_goal+i] and len(s) == len_goal:
                return True
        return False

test = Solution()
print(test.rotateString(s = "aa", goal = "a"))