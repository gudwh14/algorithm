import collections
import heapq


# v: 정점개수 , E: 간선 개수, start: 시작 정점
# 우선순위 큐를 이용하여 다익스트라!
def solution(V, E, start, infos):
    graph = collections.defaultdict(list)

    for u, v, w in infos:
        graph[u].append((v, w))

    Q = []
    # 초기 거리는 최대값으로 모두 설정
    distances = {node: float('+inf') for node in range(1, V + 1)}
    # 시작 정점의 거리는 0
    distances[start] = 0
    # 시작 정점부터 BFS 탐색 시작, 거리 비교를 위해서 거리는 1번째 인덱스로 넣음
    heapq.heappush(Q, (0, start))

    while Q:
        distance, vertex = heapq.heappop(Q)

        # 현재 거리가, 저장되어 있는 거리보다 크면 비교할 필요가 없음, 무조건 현재거리가 더 크기 때문에
        if distances[vertex] < distance:
            continue

        # 인접한 정점 거리 비교
        for adjacent in graph[vertex]:
            node, node_distance = adjacent
            new_distance = distance + node_distance
            # 해당 정점 까지의 거리가, 기존보다 더 짧으면 교체하고 Q에 넣어주기
            if distances[node] > new_distance:
                distances[node] = new_distance
                heapq.heappush(Q, (new_distance, node))

    for key, value in distances.items():
        if value == float('+inf'):
            print('INF')
        else:
            print(value)


V, E = map(int, input().split())
start = int(input())
infos = [list(map(int, input().split())) for _ in range(E)]

solution(V, E, start, infos)
