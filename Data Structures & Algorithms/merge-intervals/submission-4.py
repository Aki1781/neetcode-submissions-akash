class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        

        def merge_intervals(left, right):
            new_interval = [min(left[0], right[0]), max(left[1], right[1])]

            return new_interval

        intervals.sort(key=lambda x: x[0])
        result = []

        int_pointer, res_pointer = 1, 0
        result.append(intervals[0])

        while int_pointer < len(intervals):
            if result[res_pointer][1] >= intervals[int_pointer][0]:
                result[res_pointer] = merge_intervals(result[res_pointer], intervals[int_pointer])
                int_pointer += 1
            else:
                result.append(intervals[int_pointer])
                int_pointer += 1
                res_pointer += 1
        
        return result
