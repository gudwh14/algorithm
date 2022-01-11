import collections
import heapq
import sys
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in flights:
            graph[u].append((v, w))

        queue = []
        # 중복 방문 방지를 위해 변수 설정
        visit = {}
        heapq.heappush(queue, (0, src, 0))
        while queue:
            current_distance, node, count = heapq.heappop(queue)
            if node == dst:
                return current_distance

            # 방문객체에 없거나, 있어도 카운트가 적은거는 스킵
            if node not in visit or visit[node] > count:
                visit[node] = count
                for adjacent_node, distance in graph[node]:
                    # 최대 경유지 k 개만큼
                    if count <= k:
                        new_distance = current_distance + distance
                        heapq.heappush(queue, (new_distance, adjacent_node, count + 1))

        return -1


s = Solution()
print(s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))
print(s.findCheapestPrice(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))
print(s.findCheapestPrice(n=5, flights=[[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], src=0, dst=2,
                          k=2))
