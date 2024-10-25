class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, nums[0]]

        for idx, num in enumerate(nums[1:]):
            dp.append(max(dp[idx]+num, dp[idx+1]))

        return dp[-1]