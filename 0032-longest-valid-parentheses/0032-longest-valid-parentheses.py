class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st = [-1]

        max_length = 0

        for i,c in enumerate(s):
            if c == "(":
                st.append(i)

            else:
                st.pop()

                if not st:
                    st.append(i)

                else:
                    max_length = max(max_length,i - st[-1])

        return max_length