class Solution:
    def toLowerCase(self, s: str) -> str:
        s_list = [c for c in s]
        for i in range(len(s_list)):
            if s_list[i].isupper():
                s_list[i] = s_list[i].lower()
        return "".join(s_list)