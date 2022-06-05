'''
Author: suhejian hejiansu@126.com
Date: 2022-05-22 22:38:02
LastEditors: suhejian hejiansu@126.com
LastEditTime: 2022-06-05 21:28:43
FilePath: \LeetCode\数组\二分查找\1385.两个数组间的距离值.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        # 给定一个数，找到它可以在arr2中插入的位置, 就可以得到它和arr2的最小距离
        def findMinDistance(num ,arr2):
            arr2 = sorted(arr2)
            start, end = 0, len(arr2)
            while start < end:
                mid = start + (end - start) // 2
                if arr2[mid] == num:
                    return 0
                elif arr2[mid] < num:
                    start = mid + 1
                elif arr2[mid] > num:
                    end = mid
            
            if start == 0:
                return arr2[0] - num
            if start == len(arr2):
                return num - arr2[len(arr2) - 1]
            return min(arr2[start] - num, num - arr2[start - 1])
        
        count = 0
        for i in range(len(arr1)):
            if findMinDistance(arr1[i], arr2) > d:
                count += 1
        return count