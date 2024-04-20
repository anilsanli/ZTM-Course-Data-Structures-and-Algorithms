class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Calculate the effective rotation steps (if k > len(nums))
        k %= len(nums)

        # Reverse the entire array
        self.reverse(nums, 0, len(nums) - 1)
        # Reverse the first k elements
        self.reverse(nums, 0, k - 1)
        # Reverse the remaining elements
        self.reverse(nums, k, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


# Test cases
solution = Solution()
nums1 = [1, 2, 3, 4, 5, 6, 7]
solution.rotate(nums1, 3)
print(nums1)  # Output: [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
solution.rotate(nums2, 2)
print(nums2)  # Output: [3, 99, -1, -100]
