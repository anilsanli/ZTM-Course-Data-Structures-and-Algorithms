class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Store the index and value of each element in a dictionary to find the pair that sums up to the target
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i

# Example

# Create an instance of the Solution class
solution = Solution()

nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))  # Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9, so the indices of the pair are [0, 1]
