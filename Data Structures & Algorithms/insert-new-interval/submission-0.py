class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        

        for i,(start,end) in enumerate(intervals):
            newStart, newEnd = newInterval
            if newStart > end:
                res.append([start,end])
            elif start > newEnd:
                res.append(newInterval)
                newInterval = [start,end]
            else:
                newInterval = [min(newStart, start), max(newEnd, end)]
        res.append(newInterval)
        
        return res
        