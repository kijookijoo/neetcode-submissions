class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []

        for i in range(len(intervals)):
            if not res:
                res.append(intervals[i])
                continue
            prev = res.pop()
            if intervals[i][0] <= prev[1]:
                merged = [prev[0], max(intervals[i][1], prev[1])]
                res.append(merged)
            else:
                res.append(prev)
                res.append(intervals[i])
        
        return res
        