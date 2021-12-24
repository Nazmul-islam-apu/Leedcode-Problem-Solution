class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final = []
        def permutation(lst):
            if len(lst)==0:
                return [[]]
            if len(lst)==1:
                return [lst]
            l = []
            for i in range(len(lst)):
                m = lst[i]
                remLst = lst[:i]+lst[i+1:]
                for p in permutation(remLst):
                    l.append([m]+p)
            return l
        for p in permutation(nums):
            final.append(p)
        return final