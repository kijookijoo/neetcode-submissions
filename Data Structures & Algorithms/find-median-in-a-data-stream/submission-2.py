class MedianFinder:

    def __init__(self):
        # upper half, min heap
        self.large = []

        # lower half, max heap
        self.small = []

    def addNum(self, num: int) -> None:
        # small: [1], large: []
        # small: [1,2], large: [] -> 
        heapq.heappush(self.small, -num)
        diff = len(self.small) - len(self.large)
        if diff > 1:
            largest = heapq.heappop(self.small)
            heapq.heappush(self.large, -largest)

        while self.small and self.large and -self.small[0] > self.large[0]:
            largest_from_small = -heapq.heappop(self.small)
            smallest_from_large = heapq.heappop(self.large)

            heapq.heappush(self.large, largest_from_small)
            heapq.heappush(self.small, -smallest_from_large)

    def findMedian(self) -> float:
        total_length = len(self.small) + len(self.large)
        if total_length % 2 == 0:
            return (-self.small[0] + self.large[0]) / 2
        else:
            return float(-self.small[0])
        