class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # map each course to prerequisite first
        prereqMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            prereqMap[course].append(pre)
        
        output = []
        visited = set()
        cycle = set()

        def dfs(course) -> False:
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for pre in prereqMap[course]:
                if not dfs(pre):
                    return False 
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output
            











        
        