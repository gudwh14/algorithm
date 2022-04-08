import collections
import sys


def solution(N, graph):
    def dijkstra(start):
        visit = [-1] * (N + 1)
        max_distance = [0, 0]
        Q = collections.deque()
        Q.append(start)
        visit[start] = 0

        while Q:
            vertex = Q.popleft()

            for node, w in graph[vertex]:
                if visit[node] == -1:
                    Q.append(node)

                    visit[node] = visit[vertex] + w
                    if max_distance[0] < visit[node]:
                        max_distance = [visit[node], node]

        return max_distance

    distance, node = dijkstra(1)
    answer, node2 = dijkstra(node)
    return answer


N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    graph[v].append((u, w))
print(solution(N, graph))
