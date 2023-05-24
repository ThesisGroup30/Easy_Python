class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_sum = n * (n+1) // 2  # expected sum of 0 to n
        actual_sum = sum(nums)
        return expected_sum - actual_sum
