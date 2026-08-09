class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        heap = [-val for key,val in freq.items()]
        q = deque()
        currTime = 0
        # heap: (remaining completions)
        # q: (remaining completions, next processable time)
        heapq.heapify(heap)
        while heap or q:
            if not heap:
                currTime += q[0][1] - currTime
                
            while q and currTime >= q[0][1]:
                heapq.heappush(
                    heap, q.popleft()[0]
                )        
            
            
            if heap:
                remainder = heapq.heappop(heap)

                currTime += 1
                if remainder + 1 != 0:
                    q.append((remainder + 1, currTime + n))
        
        return currTime