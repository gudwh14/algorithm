import collections


# 음의 사이클이 존재하는지 판단하는 문제
# 벨만포드 알고리즘 사용! ( 음수의 가중치가 존재하기 때문에 )
# 시작정점을 알 수 없어 모든 정점에 대해 벨만포드 알고리즘 시행시 시간초과!
# 따라서 벨만포드 알고리즘 약간 변형
# distance[cur] != INF 조건을 제거 하면 시작정점과 관계없이 모든 간선에 대해서 업데이트
def solution(N, M, W, load, wormhole):
    INF = int(1e9)
    graph = collections.defaultdict(list)

    for S, E, T in load:
        graph[S].append((E, T))
        graph[E].append((S, T))

    for S, E, T in wormhole:
        graph[S].append((E, -T))

    distances = [INF] * (N + 1)

    def bellman_ford(start):
        distances[start] = 0

        for i in range(N):
            for node in graph:
                for v, w in graph[node]:
                    if distances[v] > distances[node] + w:
                        distances[v] = distances[node] + w

        for v in range(1, N + 1):
            for adjacent, w in graph[v]:
                if distances[adjacent] > distances[v] + w:
                    return 'YES'
        return 'NO'

    print(bellman_ford(1))


T = int(input())
for _ in range(T):
    N, M, W = map(int, input().split())
    load = [list(map(int, input().split())) for _ in range(M)]
    wormhole = [list(map(int, input().split())) for _ in range(W)]
    solution(N, M, W, load, wormhole)
