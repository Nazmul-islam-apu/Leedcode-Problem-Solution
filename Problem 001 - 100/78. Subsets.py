class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final = [[]]
        l = len(nums)
        for i in nums:
            final+=[j+[i] for j in final]
        return final