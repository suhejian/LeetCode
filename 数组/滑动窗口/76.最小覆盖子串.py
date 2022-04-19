class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        need = defaultdict(int)
        for c in t:
            need[c] += 1
        
        i = 0
        needCnt = len(t)
        ans = (0, float('inf'))
        for j, c in enumerate(s):
            # 如果是t中的字符
            if need[c] > 0:
                needCnt -= 1
            need[c] -= 1

            if needCnt == 0:
                # 此窗口已满足要求，可以考虑移动左端点
                while True:
                    if need[s[i]] == 0:
                        # 左端点是t中需要的字符, 不能再删除了
                        break
                    # 可以删除多余的左端点元素
                    need[s[i]] += 1
                    i += 1
                
                # 更新结果
                if j - i < ans[1] - ans[0]:
                    ans = (i, j)
                
                # 移动i, 重新计算
                need[s[i]] += 1
                needCnt += 1
                i += 1
        return "" if ans[1] > len(s) else s[ans[0]: ans[1] + 1]