from math import pi

class Basket:
    def __init__(self, size_=10):
        # basket의 최대 크기 디폴트 10 설정
        self.size = size_
        self.items = []
    # 만약 push 성공 시 return True, 실패 시 return False
    def push(self, item):
        if len(self.items) < self.size:
            self.items.append(item)
            return True
        return False
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()
        else:
            return False
    def getLength(self):
        return len(self.items)

class Tire:
    def __init__(self, radius_=50):
        self.radius = radius_

    def setRadius(self, radius_):
        self.radius = radius_

class Gear:
    def __init__(self, ratio_=1.5):
        self.ratio = ratio_
    
    def setRatio(self, ratio_):
        self.ratio = ratio_

class Bike:
    def __init__(self):
        self._gear = Gear()
        self._tire = Tire()
    
    def speed(self):
        return self._gear.ratio * 2 * pi * self._tire.radius

    def modifyGear(self, ratio_):
        self._gear.ratio = ratio_

    # self.gear는 protected로 직접 접근을 지양하기 때문에 getGear로 접근
    def getGear(self):
        return self._gear.ratio

class MountainBike(Bike):
    def __init__(self):
        super().__init__()
        self.ratio_list = [1, 2, 3]
        # 기어의 ratio는 디폴트로 1로 설정하고 1, 2, 3 중 변경 가능
        self._gear.ratio = 1
        self._tire.radius = 50
    
    def modifyGear(self, ratio_):
        if ratio_ in self.ratio_list:
            self._gear.ratio = ratio_

class RoadBike(Bike):
    def __init__(self):
        super().__init__()
        self._gear.ratio = 1.5
        self._tire.radius = 30

    def modifyGear(self, ratio_):
        pass

class CasualBike(Bike):
    def __init__(self):
        super().__init__()
        self.basket = Basket()
    
    def load(self, item):
        return self.basket.push(item)
    # unload 성공 시 pop된 item 객체를, 실패 시 False 리턴.
    def unload(self):
        return self.basket.pop()
        

    


        