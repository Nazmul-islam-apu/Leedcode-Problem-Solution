class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = ['@']
        i = len(s);
        flag = 0
        for x in range(i):
            j = len(l)
            if (s[x] == '(' or s[x] == '{' or s[x] == '['):
                l.append(s[x])
            elif (s[x] == ')' and l[j - 1] == '('):
                l.pop()
            elif (s[x] == '}' and l[j - 1] == '{'):
                l.pop()
            elif (s[x] == ']' and l[j - 1] == '['):
                l.pop()
            else:
                flag += 1

        if (len(l) == 1 and flag == 0):
            return True
        else:
            return False