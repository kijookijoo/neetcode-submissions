class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            total = 0
            for d in str(n):
                total += int(d) ** 2
            if total == 1:
                return True
            if total in seen:
                return False
            n = total
            seen.add(n)
        