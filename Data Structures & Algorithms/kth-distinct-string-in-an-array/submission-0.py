class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        for char in arr:
            if char not in count:
                count[char] = 0
            count[char] += 1
        
        for char in arr:
            if count[char] == 1:
                k -= 1
                if k == 0:
                    return char
        
        return ""
        
