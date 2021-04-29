class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0;
        r = len(nums) - 1;
        pos = 0
        if (target < nums[l]):
            return 0
        if (target > nums[r]):
            return (r + 1)

        while (l < r):
            mid = (l + r) // 2
            if (target == nums[mid]):
                return mid
            else:
                if (target < nums[mid]):
                    pos = mid
                    r = mid
                else:
                    pos = mid + 1
                    l = mid + 1

        return pos