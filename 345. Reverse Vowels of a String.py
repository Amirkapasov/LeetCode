class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        Glas_Bukv = ['a','e','i','o','u','A','E','I','O','U']
        s1 = [i for i in s if i in Glas_Bukv]
        s2 = s1[::-1]
        result = ''
        index = 0
        for i in s:
            if i in Glas_Bukv:
                result += s2[index]
                index += 1
            else:
                result += i
        return result

test = Solution()
print(test.reverseVowels("hello"))
