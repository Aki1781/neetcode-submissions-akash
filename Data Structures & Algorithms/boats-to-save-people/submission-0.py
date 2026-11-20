class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # brute force
            # for every person's weight i, we determine the closest pair to plkace on the boat but have the combined weight be less than limit.
            # O(n^2)
        
        # solution
            # define a left and right pointer that start at 0 and len(nums) - 1
            # we have 2 conditions:
                # if combined weight > limit --> move just right
                # if not > --> we move both
        

        count = 0
        left, right = 0, len(people) - 1
        people.sort()

        while left <= right:
            combined_weight = people[left] + people[right] #total weight 
            if left == right:
                count += 1
                break

            if combined_weight > limit:
                count += 1
                right -= 1
            else:
                count += 1
                right -= 1
                left += 1
        
        return count
