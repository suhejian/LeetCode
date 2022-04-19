class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        start, end = 0, 0
        res = 0
        window = []
        for end in range(len(s)):
            while s[end] in window:
                window.pop(0)
            
            window.append(s[end])
            res = max(res, len(window))
        
        return res