class Solution(object):
    def numberOfLines(self, widths, s):
        pixel = 0
        ans = []
        for char in s:
            w = widths[ord(char)-ord('a')]
            if pixel + w <= 100:
                pixel += w
            else:
                ans.append(pixel)
                pixel = w
        ans.append(pixel)
        return [len(ans), ans[-1]]





test = Solution()
print(test.numberOfLines(widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"))