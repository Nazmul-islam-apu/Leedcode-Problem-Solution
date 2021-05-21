class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        final = []
        if (n == 0):
            return

        for i in range(n):
            rowArray = []
            for j in range(n):
                rowArray.append(0)
            final.append(rowArray)

        count = 0;
        rowL = 0;
        rowR = n - 1;
        colD = 1;
        colU = n - 1
        while (count < n * n):
            x = rowL
            while (x <= rowR):
                final[rowL][x] = count + 1
                count += 1;
                x += 1
                if (count == (n * n)):
                    break
            if (count == (n * n)):
                break
            x = colD
            while (x <= colU):
                final[x][rowR] = count + 1
                count += 1;
                x += 1
                if (count == (n * n)):
                    break
            if (count == (n * n)):
                break
            x = rowR - 1
            while (x >= rowL):
                final[colU][x] = count + 1
                count += 1;
                x -= 1
                if (count == (n * n)):
                    break
            if (count == (n * n)):
                break
            x = colU - 1
            while (x > rowL):
                final[x][rowL] = count + 1
                count += 1;
                x -= 1
                if (count == (n * n)):
                    break
            if (count == (n * n)):
                break

            rowL += 1;
            rowR -= 1;
            colD += 1;
            colU -= 1

        return final