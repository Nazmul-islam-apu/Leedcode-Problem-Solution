class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) < 3):
            return len(nums)

        i = 1;
        track = 1
        while (i < len(nums)):
            if (nums[i] == nums[i - 1]):
                track += 1
                if (track > 2):
                    del nums[i]
                else:
                    i += 1
            else:
                track = 1
                i += 1
        return len(nums)