class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0 or s[0]=="0":
            return 0
        if len(s)==1:
            return 1
        count1 = count2 = 1
        for i in range(1,len(s)):
            count=0
            num = int(s[i])
            if num>0:
                count+=count1
            num = int(s[i-1:i+1])
            if num>=10 and num<=26:
                count+=count2
            count2 = count1
            count1 = count
        return count