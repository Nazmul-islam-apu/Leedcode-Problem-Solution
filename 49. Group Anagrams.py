from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        angrams = defaultdict(list)

        for word in strs:
            temp = sorted(word)
            angrams[''.join(temp)].append(word)

        return list(angrams.values())
