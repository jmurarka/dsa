class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        gas = 0
        for num in nums:
            if gas < 0:
                return False
            if num > gas:
                gas = num
            gas -= 1
        return True