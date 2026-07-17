class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        from bisect import bisect_right

        max_value = max(nums)

        freq = [0] * (max_value + 1)
        for value in nums:
            freq[value] += 1

        divisible_count = [0] * (max_value+1)
        exact_pairs = [0] * (max_value + 1)
        counted_pairs = [0] * (max_value + 1)
        prefix_pairs = [0] * (max_value + 1)

        for divisor in range(max_value,0,-1):
            total = 0
            larger_gcd_pairs = 0

            for multiple in range(divisor,max_value+1,divisor):
                total += freq[multiple]
                larger_gcd_pairs += exact_pairs[multiple]

            divisible_count[divisor] = total

            pair_count = total * (total - 1)//2

            counted_pairs[divisor] = pair_count

            exact_pairs[divisor] = pair_count - larger_gcd_pairs

        for value in range(1,max_value + 1):
            prefix_pairs[value] = prefix_pairs[value - 1] + exact_pairs[value]
        
        return [
            bisect_right(prefix_pairs,query)
            for query in queries
        ]