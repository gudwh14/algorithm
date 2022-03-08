import collections
import heapq


def solution(N, K, infos):
    graph = collections.defaultdict(list)

    for u, v, w in infos:
        graph[u].append((v, w))

    distances = [[float('+inf')] * K for _ in range(N + 1)]
    distances[1][0] = 0
    Q = []
    heapq.heappush(Q, (0, 1))

    while Q:
        distance, vertex = heapq.heappop(Q)

        for adjacent in graph[vertex]:
            node, node_distance = adjacent
            new_distance = distance + node_distance
            # K번째 최단경로 설정하기
            if distances[node][K - 1] > new_distance:
                distances[node][K - 1] = new_distance
                # 해당 노드에 해당하는 최단경로들을 정렬 -> K번째 최단경로 계속 만들어 주기
                distances[node].sort()
                heapq.heappush(Q, (new_distance, node))

    for idx in range(1, N + 1):
        result = distances[idx][K - 1]
        if result == float('+inf'):
            print(-1)
        else:
            print(result)


N, M, K = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
solution(N, K, infos)
