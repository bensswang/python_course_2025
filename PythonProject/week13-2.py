# Exercise 13-2 停車場系統 ParkingSystem

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        """
        建構子：
        big    : 大型車位初始數量
        medium : 中型車位初始數量
        small  : 小型車位初始數量
        """
        # 用 list 來儲存三種車位的「剩餘數量」
        # 方便讓 carType = 1, 2, 3 直接當 index 用
        # index 0 不使用，所以放 0 當占位
        self.slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        """
        carType: 1 = Big, 2 = Medium, 3 = Small
        回傳值 : 若該類型車位還有空位 → True
                 若該類型車位沒空位 → False
        """
        # 檢查指定車種的剩餘車位數是否 > 0
        if self.slots[carType] > 0:
            # 有空位：讓車停進去 → 車位數量減 1
            self.slots[carType] -= 1
            return True
        else:
            # 沒空位：無法停車
            return False
