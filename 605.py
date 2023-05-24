class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Initialize a counter for the number of flowers placed
        count = 0
        # Loop through the flowerbed array
        for i in range(len(flowerbed)):
            # Check if the current plot is empty and the previous and next plots are also empty or out of bounds
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                # If the conditions are met, plant a flower
                flowerbed[i] = 1
                count += 1
            # If the required number of flowers have been placed, return True
            if count == n:
                return True
        # If the loop completes without placing enough flowers, return False
        return False
