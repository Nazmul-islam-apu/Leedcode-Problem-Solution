class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = 0;
        r = len(nums) - 1;
        start = -1;
        end = -1
        while (l <= r):
            mid = (l + r) // 2
            if (nums[mid] >= target):
                r = mid - 1
            else:
                l = mid + 1
            if (nums[mid] == target):
                start = mid
        l = 0;
        r = len(nums) - 1
        while (l <= r):
            mid = (l + r) // 2
            if (nums[mid] <= target):
                l = mid + 1
            else:
                r = mid - 1
            if (nums[mid] == target):
                end = mid

        return [start, end]