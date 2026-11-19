class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagram --> any string that uses same letters
            # abc --> bca is valid anagram
        
        # brute force
            # O(n^3)

        # optimal solution
            # sorting --> we sort, anagrams will be the exact same string
            # O(n^2logn)

            # use [] to figure out character count and reset list
        

        count = defaultdict(list) # counter arr : [strings]

        for s in strs:
            sort_strs = [0] * 26

            for char in s:
                sort_strs[ord(char) - ord('a')] += 1
            
            count[tuple(sort_strs)].append(s)
        
        result = []

        for r in count.values():
            result.append(r)
        
        return result


s = Solution()
strs = ["act","pots","tops","cat","stop","hat"]
s.groupAnagrams(strs)
