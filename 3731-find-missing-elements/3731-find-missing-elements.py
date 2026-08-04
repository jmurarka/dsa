class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing_numbers = []
        nums.sort()

        for i in range(len(nums) - 1):
            if nums[i+1] - nums[i] > 1:
                for j in range(nums[i] + 1, nums[i+1]):
                    missing_numbers.append(j)


        return missing_numbers