class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        final = []
        l = len(intervals)
        if l == 0:
            return
        temp = [intervals[0][0], intervals[0][1]]
        for i in range(1, l):
            if intervals[i][0] <= temp[1]:
                if intervals[i][1] > temp[1]:
                    temp.pop()
                    temp.append(intervals[i][1])
            else:
                final.append(temp)
                temp = [intervals[i][0], intervals[i][1]]
        final.append(temp)
        return final
