class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a_score = 0
        for i in s:
            if i == 'A':
                a_score += 1
            if a_score >= 2:
                return False
        k = 3
        for i in range(0,len(s)+1,1):
            if s[i:k+i] == 'LLL':
                return False
        return True

test = Solution()
print(test.checkRecord("ALLL"))