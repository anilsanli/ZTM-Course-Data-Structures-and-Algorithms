class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # Array to store the maximum loot for each house
        dp = [0] * len(nums)

        # Robbing the first house
        dp[0] = nums[0]

        # Robbing the second house (or not robbing the first house)
        dp[1] = max(nums[0], nums[1])

        # Filling the dynamic programming table for the remaining houses
        for i in range(2, len(nums)):
            # Robbing house i (or not robbing house i-1)
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        # Returning the maximum loot except for the last house
        return dp[-1]


# Tests
solution = Solution()
print(solution.rob([1,2,3,1]))  # Output: 4
print(solution.rob([2,7,9,3,1]))  # Output: 12