import heapq
from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []

        for person in people:
            # 최대 힙을 만들기위해 음수로 저장
            heapq.heappush(heap, (-person[0], person[1]))

        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result

s = Solution()
print(s.reconstructQueue(people=[[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
# print(s.reconstructQueue(people=[[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))
# print(s.reconstructQueue([[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]))
