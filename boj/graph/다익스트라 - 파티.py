import collections
import heapq


def dijkstra(N, start, graph):
    distances = [float('+inf') for _ in range(N + 1)]
    distances += []
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


def solution(N, X, infos):
    answer = []
    graph = collections.defaultdict(list)

    for u, v, w in infos:
        graph[u].append((v, w))

    start_distance = [[]]
    for idx in range(1, N + 1):
        start_distance.append(dijkstra(N, idx, graph))

    end_distance = dijkstra(N, X, graph)

    for idx in range(1, N + 1):
        start = start_distance[idx][X]
        end = end_distance[idx]
        answer.append(start + end)

    answer.sort()
    return answer[-1]


N, M, X = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, X, infos))
