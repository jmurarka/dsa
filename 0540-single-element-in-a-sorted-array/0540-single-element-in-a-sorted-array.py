class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        st = 0
        end = len(nums) - 1

        if len(nums) == 1:
            return nums[0]

        while st <= end:
            mid = (end+st) // 2

            if mid + 1 <= end and nums[mid] == nums[mid+1]:
                if mid % 2 == 0:
                    st = mid + 1

                else:
                    end = mid - 1

            elif mid - 1 >= 0 and nums[mid] == nums[mid-1]:
                if mid %2 != 0:
                    st = mid + 1

                else:
                    end = mid - 1

            else:
                return nums[mid]


        return nums[0]
