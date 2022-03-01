class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i = i + 1
            j = j + 1
        if i == len(word1):
            res.extend([word2[k] for k in range(j, len(word2))])
        elif j == len(word2):
            res.extend([word1[k] for k in range(i, len(word1))])
        return "".join(res)