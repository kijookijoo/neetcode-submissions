class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for course,prereq in prerequisites:
            graph[prereq].append(course)
        
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True
            
            visited.add(node)
            path.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            path.remove(node)
            topSort.append(node)
            return True
        
        topSort = []
        visited = set()
        path = set()

        for i in range(numCourses):
            dfs(i)

        topSort.reverse()
        return topSort if len(topSort) == numCourses else []        