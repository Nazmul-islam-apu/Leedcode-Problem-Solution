class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        temp = list()
        temp.append(-1)
        count = 0;
        x = 0;
        max_length = 0
        for i in range(length):
            if (s[i] == "("):
                temp.append(i)
            else:
                temp.pop()
                if (len(temp) == 0):
                    temp.append(i)
                else:
                    max_length = max(max_length, i - temp[len(temp) - 1])

        return max_length