class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        check = [False]*length
        check[length-1] = True
        reach = length-1
        for i in range(length-2,-1,-1):
            temp = nums[i]
            if i+temp>= reach:
                check[i] = True
                reach = i
        return check[0]