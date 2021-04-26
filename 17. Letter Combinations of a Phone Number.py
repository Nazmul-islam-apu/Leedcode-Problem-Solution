class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'1': [''], '2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z'],
                 '0': [' ']}

        def combine(prev, phone, digit):
            temp = []
            for pre in prev:
                for j in phone[digit]:
                    temp.append(pre + j)
            return temp

        if digits == "":
            return []
        res = ['']
        for digit in digits:
            if digit == "1" or digit == "0":
                return []
            res = combine(res, phone, digit)
        return res