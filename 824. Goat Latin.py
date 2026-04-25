class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        res = ''
        bukv = ['a','e','i','o','u','A','E','I','O','U']
        sentence = sentence.split()
        f_sentence = [i[0] for i in sentence]
        a = 'a'
        for i in range(len(f_sentence)):
            if f_sentence[i] in bukv:
                res += sentence[i] + "ma"+a*(i+1) + ' '
            else:
                res += sentence[i][1:] + f_sentence[i]+"ma"+a*(i+1)+' '
        return res.strip()


test = Solution()
print(test.toGoatLatin('I speak Goat Latin'))