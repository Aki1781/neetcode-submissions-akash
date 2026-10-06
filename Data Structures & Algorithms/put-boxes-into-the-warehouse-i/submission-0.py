class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # important points:
            # boxes[] --> height of each box
            # warehouse[] --> height of each warehouse
        
        # count max number of boxes that we can put in warehouse

        curr_min = float("inf")

        for i in range(len(warehouse)):
            if warehouse[i] < curr_min:
                curr_min = warehouse[i]
            
            warehouse[i] = curr_min


        boxes.sort()

        w_pointer = len(warehouse) - 1
        b_pointer = 0
        count = 0

        # boxes = [1, 3, 4, 4]
        # wareho= [5, 3, 3, 3, 1]

        while w_pointer >= 0 and b_pointer < len(boxes):
            if boxes[b_pointer] <= warehouse[w_pointer]:
                count += 1
                b_pointer += 1

            w_pointer -= 1
        
        return count


        


        