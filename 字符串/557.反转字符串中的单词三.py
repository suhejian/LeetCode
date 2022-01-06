class Solution:
    def reverseWords(self, s: str) -> str:
        def inverse(word):
            return word[::-1]
        
        return " ".join([inverse(word) for word in s.split(" ")])