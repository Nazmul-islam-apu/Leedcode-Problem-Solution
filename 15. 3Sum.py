class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        # print(nums)
        l = len(nums)
        final = list()
        for i in range(l - 2):
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            left = i + 1
            right = l - 1
            while (left < right):
                target = nums[i] + nums[left] + nums[right]
                if (target > 0):
                    right -= 1
                elif (target < 0):
                    left += 1
                else:
                    final.append([nums[i], nums[left], nums[right]])
                    while (left < right and nums[left] == nums[left + 1]):
                        left += 1
                    while (left < right and nums[right] == nums[right - 1]):
                        right -= 1
                    left += 1
                    right -= 1

        return final