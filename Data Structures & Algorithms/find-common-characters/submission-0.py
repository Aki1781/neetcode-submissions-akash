class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        cnt = Counter(words[0])
        res = []

        for word in words:
            cur_cnt = Counter(word)

            for char in cnt:
                cnt[char] = min(cnt[char], cur_cnt[char])
        
        for char, freq in cnt.items():
            res.extend([char] * freq)
        
        return res