import collections

# 한 정점 x 에서 제일 거리가 먼 노드 y를 구하기
# y에서 제일 먼 거리를 구하면 트리의 최대 지름
def solution(N, infos):
    graph = collections.defaultdict(list)

    for info in infos:
        u = info[0]
        for i in range(1, len(info) - 1, 2):
            v, w = info[i:i + 2]
            graph[u].append((v, w))

    def dijkstra(vertex):
        visit = [-1] * (N + 1)
        max_distance = [0, 0]
        Q = collections.deque()
        Q.append(vertex)
        visit[vertex] = 0

        while Q:
            v = Q.popleft()

            for adjacent, w in graph[v]:
                # 방문하지 않은 인접 노드 일때
                if visit[adjacent] == -1:
                    # 큐에 넣기
                    Q.append(adjacent)
                    # distance 업데이트
                    visit[adjacent] = visit[v] + w
                    # 현재 최대 거리보다 크면 업데이트
                    if max_distance[0] < visit[adjacent]:
                        max_distance = [visit[adjacent], adjacent]

        return max_distance

    distance, node1 = dijkstra(1)
    answer, node2 = dijkstra(node1)

    return answer


N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, infos))
