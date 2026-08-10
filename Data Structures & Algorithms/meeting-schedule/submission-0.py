"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: [x.start, x.end])
        prevStart, prevEnd = math.inf, -math.inf

        for interval in intervals:
            start, end = interval.start, interval.end
            if prevStart <= start < prevEnd:
                return False
            prevStart, prevEnd = start, end
        
        return True

