class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(start,subset):
            res.append(subset[:])
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                subset.append(nums[i])
                backtrack(i+1,subset)
                subset.pop()

        nums.sort()
        res = []
        backtrack(0,[])
        return res