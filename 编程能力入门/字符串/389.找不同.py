class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic_s = {}
        dic_t = {}
        for c in s:
            dic_s[c] = dic_s.get(c, 0) + 1
        for c in t:
            dic_t[c] = dic_t.get(c, 0) + 1
        
        for c in dic_t:
            if dic_s.get(c, 0) != dic_t.get(c):
                return c
            
        # return dic_s, dic_t
