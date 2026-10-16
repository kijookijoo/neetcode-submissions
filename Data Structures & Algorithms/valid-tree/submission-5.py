class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        graph = defaultdict(list)
        for src,dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        visited = set()

        def dfs(node, path, parent):
            if node in visited:
                return True
            if node in path:
                return False
            
            path.add(node)
            for nei in graph[node]:
                if nei == parent:
                    continue
                if not dfs(nei, path, node):
                    path.remove(node)
                    return False
            path.remove(node)
            visited.add(node)
            return True
        
        for i in range(n):
            if not dfs(i, set(), -1):
                return False
        
        return True
        

            
        