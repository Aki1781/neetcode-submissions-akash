class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_fruits = 0
        count = {}
        types_count = 0
        left, right = 0, 0

        while right < len(fruits):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            if len(count.keys()) > 2:
                while left < right and len(count.keys()) > 2:
                    count[fruits[left]] -= 1

                    if count[fruits[left]] <= 0:
                        del count[fruits[left]]
                    
                    left += 1
            
            max_fruits = max(max_fruits, (right - left + 1))
            right += 1
        
        return max_fruits
                    