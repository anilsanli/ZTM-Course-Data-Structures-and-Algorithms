class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0

        # Initialize variables to keep track of minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0

        # Iterate through the prices
        for price in prices[1:]:
            # Update minimum price if the current price is lower
            min_price = min(min_price, price)
            # Update maximum profit if selling at the current price gives a higher profit
            max_profit = max(max_profit, price - min_price)

        return max_profit


# Test cases
solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5
print(solution.maxProfit([7, 6, 4, 3, 1]))  # Output: 0
