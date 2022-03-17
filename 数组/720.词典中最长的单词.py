class Solution:
    def longestWord(self, words: List[str]) -> str:
        if not words:
            return ""
        candidates = {""}
        words.sort(key = lambda x: (-len(x), x), reverse=True)
        longest = ""
        for word in words:
            if word[: -1] in candidates:
                longest = word
                candidates.add(word)
        return longest