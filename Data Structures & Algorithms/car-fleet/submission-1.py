class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i],speed[i]) for i in range(len(position))]
        # sort by furthest position, highest speed
        cars.sort(reverse=True)

        fleet = len(cars)
        stack = []
        res = []

        for i in range(len(cars)):
            pos,spd = cars[i]
            time = (target - pos) / spd
            # if the car in front takes more time to arrive, a fleet will be formed
            if stack and stack[-1] >= time:
                fleet -= 1
            else:
                stack.append(time)
        
        return fleet