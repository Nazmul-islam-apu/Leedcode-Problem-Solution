class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 1:
            return nums[l - 1]
        global_max = nums[0]
        current_max = nums[0]
        for i in range(1, l):
            current_max = max(nums[i], current_max + nums[i])
            global_max = max(current_max, global_max)

        return global_max