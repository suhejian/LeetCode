class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s2 == s1:
            return True
        if len(s1) != len(s2):
            return False
        for i in range(len(s2)):
            for j in range(i+1, len(s2)):
                s_list = [c for c in s2]
                s_list[i], s_list[j] = s_list[j], s_list[i]
                if "".join(s_list) == s1:
                    return True
        return False