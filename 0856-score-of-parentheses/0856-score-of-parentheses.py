class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        def helper(i,j):
            ans = bal = 0
            start = i

            for k in range(start,j):
                bal += 1 if s[k] == "(" else -1
                if bal == 0:
                    if k - start == 1:
                        ans += 1
                    else:
                        ans += 2 * helper(start+1,k)
                    start = k + 1
            return ans

        return helper(0,len(s))