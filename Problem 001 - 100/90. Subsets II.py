class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        final = [[]]
        res = []
        track = dict()
        for i in nums:
            final+=[j+[i] for j in final]
        #print final
        for i in final:
            if tuple(i) not in track:
                track[tuple(i)]=1
                res.append(i)
        return res