class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        nums = [i + 1 for i in range(n)]
        result = []

        def helper(nums, current, start):
            if len(current) == k:
                result.append(current[:])
                return
            if len(current) > k:
                return

            for i in range(start, n):
                helper(nums, current + [nums[i]], i + 1)

        helper(nums, [], 0)
        return result