class Solution:
    def modifyString(self, s: str) -> str:
        res = [c for c in s]
        # 三个字符就足够
        wait = "abc"
        for i in range(len(res)):
            if res[i] == '?':
                for char in wait:
                    # 有两种情况不能用当前char替换问号
                    # 其它情况都可以
                    if not (i > 0 and res[i - 1] == char or i < len(s) - 1 and res[i + 1] == char):
                        res[i] = char
                        break
        return "".join(res)
