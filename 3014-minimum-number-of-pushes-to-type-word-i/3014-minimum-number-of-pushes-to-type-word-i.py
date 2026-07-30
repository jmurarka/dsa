class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        q,r = divmod(len(word),8)
        return ((q << 2) + r) * (q+1)