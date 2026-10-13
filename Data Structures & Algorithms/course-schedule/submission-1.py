class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for a,b in prerequisites:
            graph[b].append(a)
        visited = set()
        def dfs(node, path):
            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)
            for nei in graph[node]:
                if not dfs(nei, path):
                    return False
            path.remove(node)
            visited.add(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i, set()):
                return False
        
        return True