class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def gcd(nums1,nums2):
            while nums2 != 0:
                nums1,nums2 = nums2, nums1 % nums2
            return nums1
        maxi,n = 0, len(nums)

        for i in range(n):
            maxi = max(maxi,nums[i])
            nums[i] = gcd(nums[i],maxi)

        nums.sort()

        ans = 0

        left = 0
        right = n -1 

        while left < right:
            ans += gcd(nums[left],nums[right])
            left += 1
            right -= 1

        return ans