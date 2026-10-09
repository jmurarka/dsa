class Solution:
    def minInsertions(self, s: str) -> int:
        p = 0
        n = len(s)
        k = 0

        for i in range(len(s)):
            c = s[i]
            if c == '(':
                p += 2
                if p & 1 == 1:
                    k += 1
                    p -= 1
            else:
                p -= 1
                if p < 0:
                    k += 1
                    p += 2

        return p + k