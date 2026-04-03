class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = [(position[i],speed[i]) for i in range(len(speed))]
        cars = sorted(cars, key=lambda val:val[0],reverse=True)

        curCar = cars[0]
        res = 1

        for car in cars[1:]:
            if (target - curCar[0])/curCar[1] < (target-car[0])/car[1]:
                curCar = car
                res+=1
        return res