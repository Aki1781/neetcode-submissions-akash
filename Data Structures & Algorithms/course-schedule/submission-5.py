class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        visit = set()
        safe = set()

        for i in range(numCourses):
            prereqs[i] = []
        
        for arr in prerequisites:
            pre, take = arr

            prereqs[take].append(pre)
        

        def dfs(course):
            if course in visit:
                return False
            if course in safe:
                return True
            
            visit.add(course)

            for pre in prereqs[course]:
                if not dfs(pre):
                    return False
            
            visit.remove(course)
            safe.add(course)
            
            return True
            
        for i in range(numCourses):
            if i in safe:
                continue
            if not dfs(i):
                return False
        
        return True