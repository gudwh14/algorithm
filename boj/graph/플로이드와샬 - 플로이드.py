import collections
import heapq


def solution(n, infos):
    graph = collections.defaultdict(list)
    INF = float('+inf')

    for u, v, w in infos:
        graph[u].append((v, w))

    def dijkstra(start):
        distances = [INF for _ in range(n + 1)]
        distances[start] = 0
        Q = []
        heapq.heappush(Q, (0, start))

        while Q:
            distance, vertex = heapq.heappop(Q)

            if distances[vertex] < distance:
                continue

            for adjacent in graph[vertex]:
                node, node_distance = adjacent
                new_distance = node_distance + distance
                if distances[node] > new_distance:
                    distances[node] = new_distance
                    heapq.heappush(Q, (new_distance, node))

        return distances

    result = [[]] + [dijkstra(vertex) for vertex in range(1, n + 1)]
    for vertex in range(1, n + 1):
        for node in range(1, n + 1):
            distance = result[vertex][node]
            if distance == INF:
                print(0, end=' ')
            else:
                print(distance, end=' ')
        print()


n = int(input())
m = int(input())

infos = [list(map(int, input().split())) for _ in range(m)]
solution(n, infos)
