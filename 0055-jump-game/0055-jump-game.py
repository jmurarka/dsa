class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        goal = n - 1

        for i in range(n-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False