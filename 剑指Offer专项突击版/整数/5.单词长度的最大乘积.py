class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        # words = sorted(words, key=lambda x: len(x), reverse=True)
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                a = set([c for c in words[i]])
                b = set([c for c in words[j]])
                if not (a & b): # 两个字符串不包含相同字符时
                    res = max(res, len(words[i]) * len(words[j]))
        return res