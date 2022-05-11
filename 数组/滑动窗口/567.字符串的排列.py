class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter

        counter1 = Counter(s1)
        for i in range(0, len(s2) - len(s1) + 1):
            temp = s2[i: i+len(s1)]
            counter2 = Counter(temp)
            if counter1 == counter2:
                return True
        return False