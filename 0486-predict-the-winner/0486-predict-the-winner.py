class Solution(object):
    def predictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        if ~n & 1:
            return True

        dp = [0] * n

        for i in range(n-1,-1,-1):
            dp[i] = nums[i]

            for j in range(i+1,n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j-1])

        return dp[n-1] >= 0