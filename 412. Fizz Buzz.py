class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = [i for i in range(n+1)]
        for i in res:
            if i % 3 == 0 and i % 5 == 0:
                res[i] = "FizzBuzz"
            elif i % 3 == 0:
                res[i] = "Fizz"
            elif i % 5 == 0:
                res[i] = "Buzz"
            else:
                res[i] = str(i)
        res.pop(0)
        return res

test = Solution()
print(test.fizzBuzz(15))