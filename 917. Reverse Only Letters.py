class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        slova = []
        for i in s:
            if ord(i.lower()) >= 97 and ord(i.lower()) <= 122:
                slova.append(i)
        res = ''
        for i in s:
            if not i.isalpha():
                res += i
            else:
                res += slova.pop()
        return res

test = Solution()
print(test.reverseOnlyLetters(s = "ab-cd"))