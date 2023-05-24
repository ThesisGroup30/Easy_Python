class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        duplicate = sum(nums) - sum(num_set)
        missing = (n * (n+1) // 2) - sum(num_set)
        return [duplicate, missing]
