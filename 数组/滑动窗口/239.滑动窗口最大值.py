class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 超时
        # start, end = 0, k - 1
        # res = []
        # while end < len(nums):
        #     window = nums[start: end + 1]
        #     res.append(max(window))
        #     start += 1
        #     end += 1
        
        # return res

        import heapq
        n = len(nums)
        # Python的优先队列默认是最小优先队列
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            # 确定窗口的左端点
            left = i - k + 1
            while q[0][1] < left:
                heapq.heappop(q)
            
            ans.append(-q[0][0])
        
        return ans