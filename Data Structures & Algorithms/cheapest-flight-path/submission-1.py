class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        costs = [math.inf] * n
        costs[src] = 0

        for i in range(k + 1):
            temp = costs.copy()
            for start,end,price in flights:
                if costs[start] + price <= temp[end]:
                    temp[end] = costs[start] + price
            costs = temp.copy()
        
        return costs[dst] if costs[dst] != math.inf else -1
        
        
