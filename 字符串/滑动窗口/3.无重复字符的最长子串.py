class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 暴力
        # if not s:
        #     return 0
        # length = 1
        # for i in range(len(s)):
        #     for j in range(i+1, len(s)):
        #         temp = [char for char in s[i: j+1]]
        #         if len(temp) == len(set(temp)):
        #             length = max(length, len(temp))
        #         else:
        #             break
        # return length

        # 滑动窗口
        if not s:
            return 0
        length = 1
        window = []
        for i in range(len(s)):
            # 如果该字符已经出现在窗口中
            while s[i] in window:
                window.pop(0)
            
            window.append(s[i])
            # 此时窗口内都是唯一字符
            length = max(length, len(window))
        return length