class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates)==0:
            return []
        candidates.sort()
        check = set()
        def helper(candidates,current,start):
            if sum(current)==target:
                #result.append(current[:])
                check.add(tuple(current[:]))
                return
            if sum(current)>target:
                return
            for i in range(start,len(candidates)):
                helper(candidates,current+[candidates[i]],i+1)
        helper(candidates,[],0)
        return list(check)