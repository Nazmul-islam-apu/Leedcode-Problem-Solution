from itertools import groupby


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        output = "1"
        for i in range(n - 1):
            x = output[0];
            count = 0;
            temp = list()
            for j in range(len(output)):
                if (x == output[j]):
                    count += 1
                else:
                    temp.append(str(count));
                    temp.append(str(x))
                    x = output[j];
                    count = 1
            temp.append(str(count));
            temp.append(str(x))
            output = temp
        return ''.join(output)
