class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eat(rate):
            hours = 0
            for p in piles:
                if p % rate > 0:
                    hours += 1
                hours += p // rate
            return hours
        
        res = math.inf
        l, r = 1, max(piles)
        while l <= r:
            rate = (l + r) // 2
            hours = eat(rate)
            if hours <= h:
                res = min(res, rate)
                r = rate - 1
            else:
                l = rate + 1

        return res
        