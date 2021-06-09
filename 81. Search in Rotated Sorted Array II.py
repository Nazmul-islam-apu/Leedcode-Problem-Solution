class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l = 0;
        r = len(nums) - 1
        while (l <= r):
            mid = (l + r) // 2
            if (target == nums[mid]):
                return True
            if (nums[mid] > target):
                if (nums[mid] >= nums[l] and nums[l] > target):
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if (nums[mid] <= nums[r] and nums[r] < target):
                    r = r - 1
                else:
                    l = mid + 1

        return False