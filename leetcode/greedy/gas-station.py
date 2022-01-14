from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 이동 하는 총 비용이 , 가스 충전 총량보다 크다면 출발점이 존재하지 않음
        if sum(cost) > sum(gas):
            return -1

        start, fuel = 0, 0
        for i in range(0, len(gas)):
            # 남아 있는 연료와, gas 에서 충전한 연료의 합이 코스트 보다 작다면 i는 출발점이 될수 없다
            # start + 1 해주기
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start


s = Solution()
print(s.canCompleteCircuit([1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))
