class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(numRows):
            temp = []
            for j in range(i + 1):
                if (i == 0):
                    temp.append(1)
                elif (i == 1):
                    temp.append(1)
                else:
                    if (j == 0):
                        temp.append(1)
                    elif (j == i):
                        temp.append(1)
                    else:
                        temp.append(triangle[i - 1][j - 1] + triangle[i - 1][j])

            triangle.append(temp)
        return triangle