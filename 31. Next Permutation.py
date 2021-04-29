class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums) - 1;
        x = nums[length]
        while (length >= 0):
            if (nums[length] < x):
                break
            else:
                x = nums[length]
            length -= 1
        if (length == -1):
            nums.reverse()
        else:
            i = length + 1
            x = nums[length]
            while (i < len(nums)):
                if (x >= nums[i]):
                    break
                i += 1

            temp = nums[i - 1]
            nums[i - 1] = x
            nums[length] = temp
            extra = nums[length + 1:]
            extra.sort()
            nums[length + 1:] = extra[:]
