class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ans = ""
        mods = [1] * (n - 1)
        for i in range(1, n - 1):
            mods[-i - 1] = mods[-i] * (i + 1)

        nums = [i + 1 for i in range(n)]
        for i in range(n - 1):
            nxt = (k - 1) // mods[i]
            ans += str(nums[nxt])
            nums.pop(nxt)
            k %= mods[i]

        return ans + str(nums[0])