class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m-=1
        n-=1
        x = m+n
        if m>n:
            y = n
        else:
            y = m
        def ncr(x,y):
            if y==0:
                return 1
            num,dem,op1,op2 = 1,1,x,y
            while(op2>=1):
                num*=op1
                dem*=op2
                op1-=1
                op2-=1
            val = num//dem
            return val
        final = ncr(x,y)
        return final