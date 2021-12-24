class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        final_result = list()
        for i in range(rowIndex + 1):
            val = self.ncr(rowIndex, i)
            final_result.append(val)
        return final_result

    def ncr(self, n, r):
        return (self.fact(n) / (self.fact(r) * self.fact(n - r)))

    def fact(self, x):
        res = 1
        for i in range(2, x + 1):
            res = res * i
        return res