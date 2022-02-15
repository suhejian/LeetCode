class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        n = n % len(s)
        left = s[: n]
        right = s[n: ]
        return right + left