class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {} # count of letters --> list of anagrams

        for s in strs:
            char_count = [0] * 26

            for char in s:
                index = ord(char) - ord('a')
                char_count[index] += 1
            
            if tuple(char_count) in anagrams:
                anagrams[tuple(char_count)].append(s)
            else:
                anagrams[tuple(char_count)] = []
                anagrams[tuple(char_count)].append(s)
        
        return list(anagrams.values())
