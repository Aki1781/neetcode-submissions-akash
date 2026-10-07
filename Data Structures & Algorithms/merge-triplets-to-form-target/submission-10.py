class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # info:
            # triplets --> arr of trips
            # target --> [3 elements]
        # take the max between 2 said number of triplets and try to reach our target triplet.
        
        res = [False, False, False]

            # if we can find each element in the target array seperately where each other element is not > target -1 and +1 index   
        
        for trip in triplets:
            if trip[0] == target[0] and (trip[1] <= target[1] and trip[2] <= target[2]):
                res[0] = True
            if trip[1] == target[1] and (trip[0] <= target[0] and trip[2] <= target[2]):
                res[1] = True
            if trip[2] == target[2] and (trip[1] <= target[1] and trip[0] <= target[0]):
                res[2] = True
        
        return all(res)
            


