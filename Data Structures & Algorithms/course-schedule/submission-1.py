class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prerequisite first
        prereqMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqMap[course].append(pre)
        # store course along the current dfs
        visited = set()
        cycle = set()

        def dfs(course) -> bool:
            if course in cycle:
                # cycle detected
                return False
            if course in visited:
                return True

            cycle.add(course)
            for pre in prereqMap[course]:
                if not dfs(pre):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

