class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if len(s) == 0:
            return []
        count = len(words)
        if count == 0:
            return []
        track = dict()
        for i in words:
            if i in track:
                track[i] += 1
            else:
                track[i] = 1
        l = len(words[0])

        final = []
        for i in range(len(s) - l + 1):
            new = dict()
            x = i
            for j in range(count):
                temp = s[x:x + l]
                if temp not in track:
                    break
                else:
                    if temp in new:
                        new[temp] += 1
                    else:
                        new[temp] = 1
                x += l
            if new == track:
                final.append(i)
        return final