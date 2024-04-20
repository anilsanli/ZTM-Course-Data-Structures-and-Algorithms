class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Initialize a pointer to keep track of the position to place the next non-zero element
        pointer = 0

        # Iterate through the array
        for num in nums:
            if num != 0:
                # If the current number is non-zero, move it to the pointer position
                nums[pointer] = num
                # Increment the pointer to the next position
                pointer += 1

        # Fill the remaining positions with zeros
        for i in range(pointer, len(nums)):
            nums[i] = 0


# Test cases
solution = Solution()
nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print(nums1)  # Output: [1, 3, 12, 0, 0]

nums2 = [0]
solution.moveZeroes(nums2)
print(nums2)  # Output: [0]
