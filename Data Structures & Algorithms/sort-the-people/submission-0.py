class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        heights_map = {}

        for height, name in zip(heights, names):
            heights_map[height] = name
        
        heights.sort(reverse=True)

        for index, height in enumerate(heights):
            names[index] = heights_map[height]
        
        return names

