class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        from collections import Counter
        dic = Counter([c for c in s1])
        for i in range(len(s2) - len(s1) + 1):
            temp = s2[i: len(s1) + i]
            if Counter([c for c in temp]) == dic:
                return True
        return False
