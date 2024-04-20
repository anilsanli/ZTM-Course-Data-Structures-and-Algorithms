class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Create a set to store unique elements
        unique_nums = set()

        # Iterate through the array
        for num in nums:
            # If the current number is already in the set, return True (duplicate found)
            if num in unique_nums:
                return True
            # Otherwise, add the number to the set
            else:
                unique_nums.add(num)

        # If no duplicates were found, return False
        return False


# Test cases
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 1]))  # Output: True
print(solution.containsDuplicate([1, 2, 3, 4]))  # Output: False
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # Output: True
