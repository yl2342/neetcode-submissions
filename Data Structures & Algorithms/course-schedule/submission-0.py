class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to prerequisite first
        prereqMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqMap[course].append(pre)
        # store course along the current dfs
        visiting = set()

        def dfs(course) -> bool:
            if course in visiting:
                # cycle detected
                return False
            if prereqMap[course] == []:
                return True

            visiting.add(course)
            for pre in prereqMap[course]:
                if not dfs(pre):
                    return False
            
            visiting.remove(course)
            prereqMap[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

