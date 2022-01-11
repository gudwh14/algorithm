import collections
from typing import List


# 이 문제는 그래프가 순환 구조인지를 판별하는 문제
# 순환구조이면 계속 순환하여 처리할수 없다, 순환 판별 알고리즘 구현해야함
# DFS 는 가지치기하도록 구현하는게 올바른 구현방법
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for x, y in prerequisites:
            graph[x].append(y)

        # 이미 방문했던 노드 저장, traced 에 이미 방문한 노드면 순환구조로 판단
        # 중복값을 갖지 않으므로 set 자료형으로 선언
        traced = set()
        visited = set()

        def dfs(i):
            # 순환 구조이면 False
            if i in traced:
                return False
            # 이미 방문 했던 노드이면 True
            if i in visited:
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            # 해당 노드를 이요안 모든 탐색이 끝나게 되면 방문했던 내역 을 삭제해야함
            # 형제 노드가 방문한 노드까지 남게되어, 자식노드 입장에서는 순환이라고 잘못 판단 할 수 있음
            traced.remove(i)

            # 탐색 종료후 방문 노드 추가
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True

s = Solution()
print(s.canFinish(numCourses=2, prerequisites=[[1, 0], [0, 1]]))
