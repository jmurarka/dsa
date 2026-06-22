class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        answer = float('inf')

        for ch in set(target):
            answer = min(answer,
                        s.count(ch) // target.count(ch))

        return answer