class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0;
        max_length = 0
        if (len(s) == 0):
            return count

        for i in range(len(s)):
            if (s[i] == " "):
                if (count != 0):
                    max_length = count
                count = 0
            else:
                count += 1
        if (count != 0):
            max_length = count
        return max_length