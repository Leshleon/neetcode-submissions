class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        heap = list(zip([-x for x in position], speed))
        heapq.heapify(heap)

        fleet = 1

        prev_pos, prev_sp = heapq.heappop(heap)
        prev_pos *= -1

        while heap:
            cur_pos, cur_sp = heapq.heappop(heap)
            cur_pos *= -1

            if cur_sp <= prev_sp or (target - prev_pos) / prev_sp < (prev_pos - cur_pos) / (cur_sp - prev_sp):
                fleet += 1
                prev_pos, prev_sp = cur_pos, cur_sp
        
        return fleet

        