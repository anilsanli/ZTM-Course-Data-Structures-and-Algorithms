class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return n

        # Initialize variables to store the number of ways to climb to each step
        dp = [0] * (n + 1)
        dp[1] = 1  # There's only one way to climb to the first step
        dp[2] = 2  # There are two ways to climb to the second step

        # Calculate the number of ways to climb to each step from the third step onwards
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


# Test cases
solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3
