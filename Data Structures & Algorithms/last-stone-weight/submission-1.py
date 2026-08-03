class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-1 * stones[i] for i in range(len(stones))]
        heapq.heapify(heap)

        while len(heap) >= 2:
            x = -1 * heapq.heappop(heap)
            y = -1 * heapq.heappop(heap)
            if x == y:
                continue
            else:
                heapq.heappush(heap, -1 * abs(x-y))
        
        return sum([-1 * stone for stone in heap])

        