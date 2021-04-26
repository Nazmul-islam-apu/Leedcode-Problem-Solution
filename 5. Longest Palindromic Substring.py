class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        string = ""
        length = len(s)
        if length==1:
            return s
        for i in range(len(s)):
            for j in range(length,i,-1):
                if len(string)>=(j-i):
                    break
                elif s[i:j] == s[i:j][::-1]:
                    string = s[i:j]
        return string