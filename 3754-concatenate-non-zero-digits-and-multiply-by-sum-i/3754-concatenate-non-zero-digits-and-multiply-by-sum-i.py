class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        stck = []

        while n > 0:
            rem = n % 10

            if rem != 0:
                stck.append(rem)

            n = n //10

        stck.reverse()

        x = 0

        for s in stck:
            x = x* 10 + s


        s = sum(stck)


        return x * s
        