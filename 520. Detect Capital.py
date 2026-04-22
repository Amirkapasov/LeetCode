class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        coun = 0
        sec = 0
        if word[0].islower():
            for i in word[1:]:
                if i.isupper():
                    return False
            return True
        else:
            for i in word:
                if i.islower():
                    sec += 1
        for i in word:
            if i.isupper():
                coun += 1

        return len(word) == coun or len(word) == sec+1


test = Solution()
print(test.detectCapitalUse("ffffffF"))