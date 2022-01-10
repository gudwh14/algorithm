import collections
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)

        for fr, to in sorted(tickets):
            graph[fr].append(to)

        route = []

        def dfs(start):
            while graph[start]:
                # 재방문 방지를 위해 pop 하여 원소 삭제
                # 어휘순 방문을 위해 pop(0)으로 첫번째 원소부터 읽어야한다.
                dfs(graph[start].pop(0))
            route.append(start)

        dfs('JFK')
        # 맨처음 읽었던 값이 처음에 오게하기 위해 역순으로 출력
        return route[::-1]


s = Solution()
print(s.findItinerary(tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
