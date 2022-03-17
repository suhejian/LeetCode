class Solution:
    def freqAlphabets(self, s: str) -> str:
        def numToChar(num):
            return chr(int(num) + 96)
        
        i, ans = 0, ""
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == '#':
                char = numToChar(s[i: i+2])
                ans += char
                i = i + 3
            else:
                char = numToChar(s[i])
                ans += char
                i = i + 1
        return ans