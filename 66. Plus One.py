class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits) - 1;
        carry = 1;
        new_list = list()
        while (l >= 0):
            s = digits[l] + carry
            if (s > 9):
                carry = s // 10
                digits[l] = s % 10
            else:
                carry = 0
                digits[l] = s
            if (carry == 0):
                break
            l -= 1
        if (carry > 0):
            new_list.append(carry)
            return new_list + digits

        return digits