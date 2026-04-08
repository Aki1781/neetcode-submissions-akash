class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        length = len(nums)

        for key, value in count.items():
            if value > length // 3:
                res.append(key)
        
        return res