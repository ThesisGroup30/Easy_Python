class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * n
        
        # Initializing the base cases
        dp[0], dp[1] = cost[0], cost[1]
        
        # Computing the minimum cost to reach each step
        for i in range(2, n):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        
        # Returning the minimum cost to reach the top
        return min(dp[n-1], dp[n-2])
