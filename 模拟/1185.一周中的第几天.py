class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        monthHashmap = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        total = 0
        for y in range(1971, year):
            if self.isRun(y):
                total += 366
            else:
                total += 365
        
        if self.isRun(year):
            monthHashmap[2] = 29

        for i in range(1, month):
            total += monthHashmap[i]
        
        resHashmap = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        # 1970年最后一天是星期四
        res = (total + day + 4) % 7
        return resHashmap[res]

    def isRun(self, year: int):
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
        return False