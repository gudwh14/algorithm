import collections
import heapq


def dijkstra(N, start, graph):
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
            new_distance = node_distance + distance
            if distances[node] > new_distance:
                distances[node] = new_distance
                heapq.heappush(Q, (new_distance, node))

    return distances


def solution(N, infos, v1, v2):
    graph = collections.defaultdict(list)

    for u, v, w in infos:
        graph[u].append((v, w))
        graph[v].append((u, w))

    start_distances = dijkstra(N, 1, graph)
    v1_distances = dijkstra(N, v1, graph)
    v2_distances = dijkstra(N, v2, graph)

    answer = min(start_distances[v1] + v1_distances[v2] + v2_distances[N],
                 start_distances[v2] + v2_distances[v1] + v1_distances[N])

    if answer == float('+inf'):
        return -1
    return answer


N, E = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(E)]
v1, v2 = map(int, input().split())
print(solution(N, infos, v1, v2))
