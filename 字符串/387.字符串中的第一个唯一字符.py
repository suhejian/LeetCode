class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        for i in range(len(s)):
            char = s[i]
            if char not in hashmap:
                hashmap[char] = [False, i]
            else:
                hashmap[char] = [True, i]
        res = -1
        for key in hashmap:
            value = hashmap[key]
            if value[0] == False:
                res = value[1]
                return res
        return res
