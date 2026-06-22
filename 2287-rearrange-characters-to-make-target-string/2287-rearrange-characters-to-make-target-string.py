class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        f = Counter(s)

        return min(f[c] // count for c,count in Counter(target).items())