class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # index --> current i - updating index

        # stack = [38, 1]
        # [1, 4, 1, 1, 2, ]


        stack = []
        res = [0] * len(temperatures)


        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                days = i - stack[-1][1]
                res[stack[-1][1]] = days
                stack.pop()
            
            stack.append([temperatures[i], i])
        
        return res
            
