class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if (m == 0):
            return
        n = len(matrix[0])

        i = 0;
        rowL = 0;
        rowR = n - 1;
        colD = 1;
        colU = m - 1
        spiral = list();
        count = 0
        while (True):
            x = rowL
            while (x <= rowR):
                spiral.append(matrix[rowL][x])
                x += 1;
                count += 1
                if (count == (m * n)):
                    break
            if (count == (m * n)):
                break

            x = colD
            while (x <= colU):
                spiral.append(matrix[x][rowR])
                x += 1;
                count += 1
                if (count == (m * n)):
                    break
            if (count == (m * n)):
                break

            x = rowR - 1
            while (x >= rowL):
                spiral.append(matrix[colU][x])
                x -= 1;
                count += 1
                if (count == (m * n)):
                    break

            if (count == (m * n)):
                break

            x = colU - 1
            while (x >= colD):
                spiral.append(matrix[x][rowL])
                x -= 1;
                count += 1
                if (count == (m * n)):
                    break

            rowL += 1;
            colD += 1;
            rowR -= 1;
            colU -= 1
            if (count == (m * n)):
                break
        return spiral