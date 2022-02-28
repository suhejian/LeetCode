class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # 两点确定一直线
        if len(coordinates) == 2:
            return True
        # k = (y1 - y0) / (x1 - x0)
        # b = y1 - k * x1
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        if x1 == x0:
            for i in range(2, len(coordinates)):
                x, y = coordinates[i]
                if x != x1:
                    return False
            return True
        k = (y1 - y0) / (x1 - x0)
        b = y1 - k * x1

        for i in range(2, len(coordinates)):
            x, y = coordinates[i]
            if y != k * x + b:
                return False
        return True