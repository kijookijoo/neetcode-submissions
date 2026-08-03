class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        maxProfit = 0

        for i in range(len(prices)):
            cheapest = min(cheapest, prices[i])
            maxProfit = max(maxProfit, prices[i] - cheapest)
    
        return maxProfit