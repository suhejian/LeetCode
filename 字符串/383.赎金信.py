class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        from collections import Counter
        counter = Counter(ransomNote)
        for char in magazine:
            # 该字符可以在ransomNote中使用时，就减去一个
            if char in counter:
                counter[char] -= 1
        res = True
        for value in counter:
            if counter[value] > 0:
                res = False
                break
        return res