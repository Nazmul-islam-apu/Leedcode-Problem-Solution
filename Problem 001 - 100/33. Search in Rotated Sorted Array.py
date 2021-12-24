class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        low = 0;
        high = len(nums) - 1;
        mid = (low + high) // 2
        while (low <= high):
            mid = (low + high) // 2
            if (target == nums[mid]):
                return mid

            if (nums[low] <= nums[mid]):
                if (nums[low] <= target and nums[mid] >= target):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (nums[mid] <= target and nums[high] >= target):
                    low = mid + 1
                else:
                    high = mid - 1

        return -1