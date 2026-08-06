class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        def gcd(a,b):
            while b:
                a,b = b, a%b
            return a
        q = n // 10
        r = n % 10

        req = t // gcd(max(q,1),t)
        nxt = ((r + req - 1) // req) * req
        x = nxt - (nxt - 10) * (nxt // 10)

        return q * 10 + x 