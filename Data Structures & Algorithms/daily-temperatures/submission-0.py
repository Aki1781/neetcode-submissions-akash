class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # [30, 38, 30, 36, 35, 40, 28] --> [1, 4, 1, 2, 1, 0, 0]
        # BF --> O(n^2)
        # 2 pointer:
        # [30, 38, 30, 36, 35, 40, 28] 
        #      l    r
        # [[38, 1], [36, 3], [35, 4]]
        # [1, ]

        stack = []
        res = [0] * len(temperatures)
        

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                temp, index = stack.pop()
                days = i - index
                res[index] = days
            
            stack.append([temperatures[i], i])
        
        return res