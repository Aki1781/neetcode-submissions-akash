class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        repeat_tracker = set()
        left = 0

        for right in range(len(s)):
            while s[right] in repeat_tracker:
                repeat_tracker.remove(s[left])
                left += 1
            repeat_tracker.add(s[right])
            res = max(res, right - left + 1)
        
        return res