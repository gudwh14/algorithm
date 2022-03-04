import collections
import heapq


def solution(N, M, infos, start, end):
    graph = collections.defaultdict(list)

    for u, v, w in infos:
        graph[u].append((v, w))

    distances = [float('+inf') for _ in range(N + 1)]
    distances[start] = 0
    Q = []
    heapq.heappush(Q, (0, start))

    while Q:
        distance, vertex = heapq.heappop(Q)

        if distances[vertex] < distance:
            continue

        for adjacent in graph[vertex]:
            node, node_distance = adjacent
            new_distance = distance + node_distance
            if distances[node] > new_distance:
                distances[node] = new_distance
                heapq.heappush(Q, (new_distance, node))

    return distances[end]


N = int(input())
M = int(input())
infos = [list(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())

print(solution(N, M, infos, start, end))
