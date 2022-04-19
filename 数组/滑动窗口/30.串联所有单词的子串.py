class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        start = 0
        window = []
        res = []
        for end in range(len(words) * len(words[0]), len(s) + 1):
            window = s[start: end]
            elements = [window[i: i + len(words[0])] for i in range(0, len(window), len(words[0]))]
            if sorted(elements) == sorted(words):
                # 符合要求
                res.append(start)
            start += 1
        return res
