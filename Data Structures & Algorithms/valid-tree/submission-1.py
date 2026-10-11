class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        graph = defaultdict(list)
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, path, parent):
            if node in path:
                return False
            if node in visited:
                return True
            
            path.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, path, node):
                    return False
            path.remove(node)
            visited.add(node)
            return True
        
        for i in range(n):
            if not dfs(i, set(), -1):
                return False
        
        return True
        