class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            letter_map = [0] * 26
            for char in word:
                letter_map[ord(char) - ord('a')] += 1
            groups[tuple(letter_map)].append(word)
        
        return list(groups.values())

