class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        if (len(nums) == 0):
            return result

        array = set(nums)
        while result in array:
            result += 1
        return result
