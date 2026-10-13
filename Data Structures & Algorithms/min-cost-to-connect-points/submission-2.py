class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if len(points) == 1:
            return 0
        heap = []

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                heap.append((dist, i, j))
        
        heapq.heapify(heap)
        n = len(points)
        cost = 0
        roots = [-1] * n

        def find_parent(node):
            if roots[node] == -1:
                return node
            return find_parent(roots[node])

        while heap:
            weight, node1, node2 = heapq.heappop(heap)
            p1, p2 = find_parent(node1), find_parent(node2)
            if p1 == p2:
                continue
            roots[p2] = p1
            
            cost += weight
        
        return cost




        