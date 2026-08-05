class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        g = 1
        cars = []
        for i in range(len(speed)):
            cars.append((position[i], speed[i]))
        cars.sort(key = lambda x: x[0])

        def time_needed(car):
            d = target - car[0]
            time = float(d) / float(car[1])
            return time
        i = len(cars) - 2
        arriveTime = time_needed(cars[-1])
        while i >= 0:
            car = cars[i]
            if time_needed(car) > arriveTime:
                g += 1
                arriveTime = time_needed(car)
            i -= 1
        return g


