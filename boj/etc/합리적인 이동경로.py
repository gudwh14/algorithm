import heapq


def solution(N, M, graph):
    # 도착지 2에서부터 정점까지의 최소거리를 구하기
    Q = []
    distances = [float('inf')] * (N + 1)
    heapq.heappush(Q, (0, 2))

    distances[2] = 0

    while Q:
        cost, vertex = heapq.heappop(Q)

        if distances[vertex] < cost:
            continue

        for node, c in graph[vertex]:
            new_cost = cost + c
            if distances[node] > new_cost:
                distances[node] = new_cost
                heapq.heappush(Q, (new_cost, node))

    # dp[i] : i번 노드에서 2번까지 합리적인 이동경로 개수
    dp = [-1] * (N + 1)

    def move(vertex):
        # 이미 방문한 노드 일경우
        if dp[vertex] != -1:
            return dp[vertex]
        # 2번 노드에 도착할경우, 1개의 경우가 생긴다 return 1
        if vertex == 2:
            dp[vertex] = 1
            return 1
        # 첫 방문시, 현재 노드에서 합리적인 이동경로는 0개이다
        dp[vertex] = 0

        # 인접노드 방문
        for adjacent, cost in graph[vertex]:
            # 현재 노드에서 목적지까지 거리보다, 인접노드에서 목적지까지 거리가 가까우면 탐색
            if distances[vertex] > distances[adjacent]:
                dp[vertex] += move(adjacent)

        return dp[vertex]

    return move(1)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, c = map(int, input().split())
    graph[u].append([v, c])
    graph[v].append([u, c])

print(solution(N, M, graph))
