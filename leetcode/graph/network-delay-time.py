import collections
import heapq
import sys
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # 초기 거리 배열 설정 (무한대에 해당하는 최대값으로 설정하면 됨)
        distances = {node: sys.maxsize for node in range(1, n + 1)}
        # 시작 노드 거리 0 으로 설정
        distances[k] = 0
        # 탐색을 위한 큐
        queue = []

        # 우선순위 큐를 이용하여 push (거리, 노드) 순으로 넣어야함, heapq 모듈은 첫번째 데이터를 기준으로 정렬을 진행하기 때문!
        heapq.heappush(queue, (distances[k], k))

        while queue:
            # 탐색할 노드, 거리를 가져옴
            current_distance, node = heapq.heappop(queue)
            # 기존에 있는 거리보다 길다면 탐색 X
            if distances[node] < current_distance:
                continue

            # 인접 노드 탐색
            for adjacent_node, distance in graph[node]:
                # 현재 노드에서 인접 노드를 지나가는 거리를 합
                new_distance = current_distance + distance
                # 새로운 거리가, 기존 거리보다 짧으면 변경
                # 다음 인접노드의 거리를 계산하기위 해서 큐 에 삽입
                if new_distance < distances[adjacent_node]:
                    distances[adjacent_node] = new_distance
                    heapq.heappush(queue, (new_distance, adjacent_node))

        if max(distances.values()) == sys.maxsize:
            return -1
        else:
            return max(distances.values())



class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        # 수도코드와 다르게 초기값으로 무한대로 설정하지 않는다. heapq 모듈의 기능상 제약때문
        distances = collections.defaultdict(int)
        # 탐색을 위한 큐
        queue = []

        # 우선순위 큐를 이용하여 push (거리, 노드) 순으로 넣어야함, heapq 모듈은 첫번째 데이터를 기준으로 정렬을 진행하기 때문!
        heapq.heappush(queue, (0, k))

        while queue:
            # 탐색할 노드, 거리를 가져옴
            current_distance, node = heapq.heappop(queue)

            # distances 에 아무값도 셋팅하지 않았기 때문에 처음에는 비어있을것이다, 이 경우에만 힙에 푸시하는 형태
            # distances 에는 항상 최솟값만 셋팅될 것이다
            if node not in distances:
                distances[node] = current_distance
                # 인접 노드 탐색
                for adjacent_node, distance in graph[node]:
                    # 현재 노드에서 인접 노드를 지나가는 거리를 합
                    new_distance = current_distance + distance
                    heapq.heappush(queue, (new_distance, adjacent_node))

        if len(distances) == n:
            return max(distances.values())
        return -1


s = Solution()
print(s.networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(s.networkDelayTime(times = [[1,2,1]], n = 2, k = 2))