class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        tracker = set()
        tracker.add(s[0])

        left, right = 0, 1
        max_length = 1

        while left <= right and right < len(s):
            # add right to set if:
                # s[right] is NOT in the set already
                # if it is --> loop until s[left] in no longer in set
                # if its not --> add it to set and update out final length
                # zxyzxy
            if s[right] in tracker:
                while left < right and left < len(s) and s[right] in tracker:
                    tracker.remove(s[left])
                    left += 1
            else:
                tracker.add(s[right])
                max_length = max(max_length, (right - left) + 1 )
                right += 1
        
        return max_length