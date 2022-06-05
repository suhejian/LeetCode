'''
Author: suhejian hejiansu@126.com
Date: 2022-05-22 22:55:04
LastEditors: suhejian hejiansu@126.com
LastEditTime: 2022-06-05 21:27:04
FilePath: \LeetCode\数组\二分查找\633.平方数之和.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
'''
Author: suhejian hejiansu@126.com
Date: 2022-05-22 22:55:04
LastEditors: suhejian hejiansu@126.com
LastEditTime: 2022-06-05 21:26:58
FilePath: \LeetCode\数组\二分查找\633.平方数之和.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)
        while left <= right:
            cur = left * left + right * right
            if cur == c: 
                return True
            if cur < c:
                left += 1
            else:
                right -= 1
        return False