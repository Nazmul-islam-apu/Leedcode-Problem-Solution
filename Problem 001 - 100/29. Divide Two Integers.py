class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == 0:
            return 0
        if(dividend<0 and divisor<0):
            sign = +1
        if(dividend<0 and divisor>0):
            sign = -1
        if(dividend>0 and divisor<0):
            sign = -1
        if(dividend>0 and divisor>0):
            sign = +1
        final = abs(dividend)//abs(divisor)
        final = final*sign
        if(final>(2**31-1)):
            return (2**31-1)
        elif(final<-(2**31)):
            return -(2**31)
        else:
            return final