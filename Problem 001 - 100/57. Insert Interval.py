class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        l = len(intervals)
        if l == 0:
            return [newInterval]
        i = 0;
        inserted = "False"
        x = newInterval[0];
        y = newInterval[1]
        final = []
        temp = []
        while (i < l):
            p = intervals[i][0];
            q = intervals[i][1]
            if inserted == "False":
                if x < p:
                    if y < p:
                        final.append([x, y])
                        final.append([p, q])
                        inserted = "True"
                    elif y >= p and y <= q:
                        final.append([x, q])
                        inserted = "True"
                    else:
                        final.append([x, y])
                        inserted = "True"
                elif x >= p and x <= q:
                    if y <= q:
                        final.append([p, q])
                        inserted = "True"
                    else:
                        final.append([p, y])
                        inserted = "True"
                else:
                    final.append([p, q])
            else:
                temp = final[-1]
                if p > temp[1]:
                    final.append([p, q])
                elif p == temp[1]:
                    temp = [temp[0], q]
                    final.pop()
                    final.append(temp)
                elif p < temp[1]:
                    if q >= temp[1]:
                        temp = [temp[0], q]
                        final.pop()
                        final.append(temp)

            i += 1
        if inserted == "False":
            temp = final[-1]
            if x <= temp[1]:
                if y >= temp[1]:
                    temp = [temp[0], y]
                    final.pop()
                    final.append(temp)
            else:
                final.append([x, y])

        # print final
        return final