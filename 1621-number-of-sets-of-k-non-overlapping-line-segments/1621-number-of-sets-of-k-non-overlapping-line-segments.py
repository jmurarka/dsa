class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        def mod_pow(base,exp):
            result = 1

            while exp > 0:
                if exp & 1:
                    result = result * base % MOD

                base = base * base % MOD

                exp >>= 1

            return result

        N = n + k - 1
        R = 2 * k

        R = min(R,N-R)

        numerator = 1
        denominator = 1

        for i in range(1,R + 1):
            numerator = numerator * (N - R + i) % MOD
            denominator = denominator * i % MOD

        inverse_denominator = mod_pow(denominator,MOD - 2)

        return numerator * inverse_denominator % MOD