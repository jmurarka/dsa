class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        cnt = 0

        for s in patterns:
            if word.find(s) != -1:
                cnt += 1

        return cnt