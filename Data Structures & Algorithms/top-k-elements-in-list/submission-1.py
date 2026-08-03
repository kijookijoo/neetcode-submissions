class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for key,val in Counter(nums).items():
            heap.append([-val,key])

        res = []
        heapq.heapify(heap)
        for i in range(k):
            _, num = heapq.heappop(heap)
            res.append(num)
        return res
        