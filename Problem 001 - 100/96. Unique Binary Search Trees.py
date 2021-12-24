class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        def factorial(x):
            num = 1
            for i in range(1, x + 1):
                num *= i
            return num

        return (factorial(2 * n) // (factorial(n + 1) * factorial(n)))