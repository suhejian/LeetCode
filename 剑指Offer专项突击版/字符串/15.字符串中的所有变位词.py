class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        dic = Counter([c for c in p])

        res = []
        for i in range(len(s) -len(p) + 1):
            temp = s[i: i + len(p)]
            if Counter([c for c in temp]) == dic:
                res.append(i)
        return res