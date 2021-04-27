class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        h = len(haystack);
        n = len(needle)
        i = j = 0
        if (n == 0):
            return 0

        while (i < h and j < n):
            if (haystack[i] == needle[j]):
                j += 1;
                i += 1
            else:
                i = i - j + 1
                j = 0
        if (j == n):
            return (i - j)
        else:
            return -1