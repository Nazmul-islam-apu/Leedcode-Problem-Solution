class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        final = 0

        if num1 == "0" or num2 == "0":
            return "0"
        first = len(num1)
        second = len(num2)
        for i in range(first - 1, -1, -1):
            temp = 0
            x = 0
            carry = 0
            for j in range(second - 1, -1, -1):
                multiply = (int(num2[j]) * int(num1[i])) + carry
                temp += ((multiply % 10) * (10 ** x))
                carry = multiply // 10
                x += 1
            if carry != 0:
                temp += (carry * (10 ** x))
            temp = temp * (10 ** (first - i - 1))
            final += temp
        return str(final)