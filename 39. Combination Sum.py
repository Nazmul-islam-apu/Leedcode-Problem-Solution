class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def helper(current, start):
            if sum(current) == target:
                result.append(current[:])
                return
            if sum(current) > target:
                return
            for i in range(start, len(candidates)):
                helper(current + [candidates[i]], i)

        result = []
        helper([], 0)
        return result