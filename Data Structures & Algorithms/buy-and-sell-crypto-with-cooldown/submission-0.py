class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}

        def dp(i, is_holding):
            if i >= len(prices):
                return 0 if not is_holding else -math.inf
            key = (i, is_holding)
            if key in cache:
                return cache[key]

            if is_holding:
                # when already possessing a share, you can choose to sell or skip
                cache[key] = max(
                    dp(i + 1, True),
                    dp(i + 2, False) + prices[i],
                )
            else:
                # buy or skip
                cache[key] = max(
                    dp(i + 1, True) - prices[i],
                    dp(i + 1, False)
                )

            return cache[key]
        
        return dp(0, False)


        