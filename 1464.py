class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize two variables to store the two largest numbers in the array
        largest1 = largest2 = float('-inf')
        # Loop through the array and update the two largest numbers
        for num in nums:
            if num > largest1:
                largest2 = largest1
                largest1 = num
            elif num > largest2:
                largest2 = num
        # Return the product of the two largest numbers minus 1
        return (largest1 - 1) * (largest2 - 1)
