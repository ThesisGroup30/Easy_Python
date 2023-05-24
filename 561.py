class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # Sort the array in ascending order
        result = 0
        
        # Sum every other element starting from index 0
        for i in range(0, len(nums), 2):
            result += nums[i]
        
        return result