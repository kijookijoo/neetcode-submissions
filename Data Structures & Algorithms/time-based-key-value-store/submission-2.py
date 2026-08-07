class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:        
        curr = self.timemap[key]
        if not curr:
            return ""
        l, r = 0, len(curr) - 1
        idx = 0

        while l <= r:
            mid = (l + r) // 2
            time,val = curr[mid]

            if time <= timestamp:
                idx = max(idx, mid)
                l = mid + 1
            else:
                r = mid - 1
        
        return "" if curr[idx][0] > timestamp else curr[idx][1]


        
