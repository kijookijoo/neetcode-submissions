class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        global_visited = set()
        graph = defaultdict(list)
        for src,dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)

        def dfs(node):
            nonlocal global_visited
            if node in global_visited:
                return False
            
            global_visited.add(node)
            for nei in graph[node]:
                dfs(nei)
            return True

        res = 0
        for i in range(n):
            if dfs(i):
                res += 1
        
        return res
        