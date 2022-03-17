class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        counter_s = Counter(s)
        conuter_t = Counter(t)
        
        res = counter_s == conuter_t
        return res