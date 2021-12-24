class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        final = set()
        def permutation(array):
            if len(array)==0:
                return []
            if len(array)==1:
                return [array]
            temp = []
            for i in range(len(array)):
                new = array[i]
                rem_list = array[:i]+array[i+1:]
                for x in permutation(rem_list):
                    temp.append([new]+x)
            return temp
        for p in permutation(nums):
            final.add(tuple(p))
        return list(list(x) for x in final)