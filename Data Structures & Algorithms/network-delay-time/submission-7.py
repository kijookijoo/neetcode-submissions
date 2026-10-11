class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for a,b,time in times:
            graph[a].append((b, time))
        
        dists = {}
        for i in range(1, n + 1):
            dists[i] = math.inf
        heap = [(0,k)]

        while heap:
            weight, node = heapq.heappop(heap)
            if weight < dists[node]:
                dists[node] = weight
            else:
                continue
            for nei,dist_to_nei in graph[node]:
                new_dist = weight + dist_to_nei
                if dists[nei] >= new_dist:
                    heapq.heappush(heap, (dist_to_nei + weight, nei))

        res = -math.inf
        for _,time in dists.items():
            if time == math.inf:
                return -1
            res = max(res, time)
        return res
                


        