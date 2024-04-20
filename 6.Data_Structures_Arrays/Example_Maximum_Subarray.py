class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = nums[0]
        current_sum = nums[0]

        for num in nums[1:]:
            # Either start a new subarray or extend the current subarray
            current_sum = max(num, current_sum + num)
            # Update the maximum sum encountered so far
            max_sum = max(max_sum, current_sum)

        return max_sum


# Test cases
solution = Solution()
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Output: 6
print(solution.maxSubArray([1]))  # Output: 1
print(solution.maxSubArray([5, 4, -1, 7, 8]))  # Output: 23
