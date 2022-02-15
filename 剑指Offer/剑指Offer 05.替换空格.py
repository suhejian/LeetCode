class Solution:
    def replaceSpace(self, s: str) -> str:
        tokens = s.split(" ")
        return "%20".join(tokens)