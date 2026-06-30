class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(pos, speed)), reverse=True)
        fleet, fleet_time = 0, 0

        for pos, speed in cars:
            time = (target - pos) / speed

            if time > fleet_time:
                fleet += 1
                fleet_time = time

        return fleet