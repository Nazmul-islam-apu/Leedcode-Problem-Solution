class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s)==0):
            return True
        l = len(s); new=""
        for i in s:
            if(i.isalpha()):
                new+=i.lower()
            elif(i.isnumeric()):
                new+=i.lower()
        s = new[::-1]
        if(new==s):
            return True
        else:
            return False