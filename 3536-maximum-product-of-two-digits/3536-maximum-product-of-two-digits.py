class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """

        
        n = str(n)
        n = sorted(n)

        if not n:
            return 0

        p1 = int(n[-2])
        p2 = int(n[-1])

        return p1 * p2