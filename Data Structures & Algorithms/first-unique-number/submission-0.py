class FirstUnique:

    def __init__(self, nums: List[int]):
        self.unique_map = Counter(nums)
        

    def showFirstUnique(self) -> int:
        for key, val in self.unique_map.items():
            if val == 1:
                return key
        return -1

    def add(self, value: int) -> None:
        if value in self.unique_map:
            self.unique_map[value] += 1
        else:
            self.unique_map[value] = 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
