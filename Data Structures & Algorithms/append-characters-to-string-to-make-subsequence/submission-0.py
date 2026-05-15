class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_point = 0
        t_point = 0

        while s_point < len(s) and t_point < len(t):
            if s[s_point] == t[t_point]:
                t_point += 1
            s_point += 1
        
        return len(t) - t_point
            