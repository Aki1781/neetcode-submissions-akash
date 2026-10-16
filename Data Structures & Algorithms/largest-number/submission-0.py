from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        def compare(a, b):
            ab = str(a) + str(b)
            ba = str(b) + str(a)

            if ab > ba:
                return -1
            elif ba > ab:
                return 1
            
            return 1
        
        nums.sort(key=cmp_to_key(compare))

        return str(int(''.join(map(str, nums))))