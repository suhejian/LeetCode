class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.num_big = big
        self.num_medium = medium
        self.num_small = small


    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.num_big > 0:
                self.num_big -= 1
                return True
            else:
                return False
        if carType == 2:
            if self.num_medium > 0:
                self.num_medium -= 1
                return True
            else:
                return False
        
        if carType == 3:
            if self.num_small > 0:
                self.num_small -= 1
                return True
            else:
                return False



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)