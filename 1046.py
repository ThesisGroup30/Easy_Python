class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            # sort stones in descending order
            stones.sort(reverse=True)
            
            # get the two heaviest stones
            stone1, stone2 = stones[0], stones[1]
            
            # remove the two heaviest stones
            stones.remove(stone1)
            stones.remove(stone2)
            
            # smash the two heaviest stones and add the result to stones
            if stone1 != stone2:
                stones.append(stone1 - stone2)
        
        # return the weight of the last remaining stone, or 0 if no stones are left
        return stones[0] if stones else 0
