class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = 0
        l = len(prices)
        temp = 0
        for i in range(1,l):
            if (prices[i]-prices[buy])>temp:
                    temp = prices[i]-prices[buy]
            else:
                profit+=temp
                temp = 0
                buy = i
        if temp>0:
            profit+=temp
        return profit