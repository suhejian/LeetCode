class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        res = -1
        min_dis = 10 ** 5
        for i, point in enumerate(points):
            a, b = point[0], point[1]
            if a == x or b == y:
                dis = abs(a - x) + abs(b - y)
                if dis < min_dis:
                    min_dis = dis
                    res = i 
        return res