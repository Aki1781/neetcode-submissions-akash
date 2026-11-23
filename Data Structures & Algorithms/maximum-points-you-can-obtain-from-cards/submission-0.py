class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        current = sum(cardPoints[:k])
        best = current

        for i in range(1, k + 1):
            current -= cardPoints[k - i]
            current += cardPoints[n - i]
            best = max(best, current)

        return best