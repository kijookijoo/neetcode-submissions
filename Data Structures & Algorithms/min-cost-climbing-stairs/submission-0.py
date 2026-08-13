class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # map each index to min amt of cost needed to reach the end
        cache = {}

        def dp(i):
            if i > len(cost):
                # overshoot, should disregard 
                return math.inf
            if i == len(cost):
                return 0
            if i in cache:
                return cache[i]

            cache[i] = min(dp(i + 1) + cost[i], dp(i + 2) + cost[i])

            return cache[i]
        
        return min(dp(0), dp(1))
            

        