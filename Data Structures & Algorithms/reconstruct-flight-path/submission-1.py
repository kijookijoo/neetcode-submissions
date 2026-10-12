class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for src, dst in sorted(tickets, reverse=True):
            graph[src].append(dst)

        res = []

        def dfs(node):
            while graph[node]:
                nei = graph[node].pop()
                dfs(nei)
            res.append(node)

        dfs("JFK")
        return res[::-1]