class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x<2:
            return x
        lo = 0; hi =x
        while (hi-lo)>1:
            mid = (lo+hi)//2
            if (mid*mid)>x:
                hi = mid
            else:
                lo = mid
        return (lo+hi)//2