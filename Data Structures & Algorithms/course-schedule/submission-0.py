class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = defaultdict(list)
        for course,prereq in prerequisites:
            preMap[course].append(prereq)
        
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            return True
        
        for course,prereq in prerequisites:
            if not dfs(course):
                return False
        return True

