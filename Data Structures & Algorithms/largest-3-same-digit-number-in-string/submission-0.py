class Solution:
    def largestGoodInteger(self, num: str) -> str:
        window = deque()
        res = -math.inf
        for i,c in enumerate(num):
            if i < 3:
                window.append(c)
                continue
            
            window.popleft()
            window.append(c)
            if len(set(window)) == 1:
                if int(c) > res:
                    res = int(c)

        return str(res) * 3 if res != -math.inf else ""
        