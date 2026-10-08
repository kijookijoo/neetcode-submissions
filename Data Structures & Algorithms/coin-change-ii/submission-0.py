class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}

        def dp(i, remaining):
            # (i, remaining) mapped to the num of ways in which the target can be reached starting
            # from that index
            if i == len(coins):
                return 1 if remaining == 0 else 0
            if remaining < 0:
                return 0
            key = (i, remaining)
            if key in cache:
                return cache[key]
            
            # 3 branches: include and stay, include and move on, skip
            cache[key] = dp(i, remaining - coins[i]) + dp(i + 1, remaining)
            return cache[key]    

        return dp(0, amount)    