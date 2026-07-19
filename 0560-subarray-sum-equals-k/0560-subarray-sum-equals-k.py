class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix_sum = 0
        count = 0

        prefix_map = {0:1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in prefix_map:
                count += prefix_map[prefix_sum - k]

            prefix_map[prefix_sum] = 1 + prefix_map.get(prefix_sum,0)

        return count