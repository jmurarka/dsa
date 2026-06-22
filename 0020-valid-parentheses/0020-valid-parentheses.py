class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stck = []

        for ch in s:

            if ch == "(" or ch == "[" or ch == "{":
                stck.append(ch)

            else:
                if not stck:
                    return False

                top = stck.pop()

                if ch == ")" and top != "(":
                    return False

                if ch == "]" and top != "[":
                    return False

                if ch == "}" and top != "{":
                    return False

        return len(stck) == 0

