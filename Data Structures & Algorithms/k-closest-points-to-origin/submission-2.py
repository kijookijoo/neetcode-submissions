class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            dist = math.sqrt((x**2) + (y**2))
            heap.append((dist, (x,y)))
        
        res = []
        heapq.heapify(heap)
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        
        