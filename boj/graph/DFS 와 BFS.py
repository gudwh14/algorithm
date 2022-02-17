import collections


# DFS 탐색
def dfs(v, graph, visit):
    visit.append(v)

    for adjacent in graph[v]:
        if adjacent not in visit:
            dfs(adjacent, graph, visit)


# BFS 탐색
def bfs(start, graph, visit):
    Q = collections.deque()
    Q.append(start)

    while Q:
        v = Q.popleft()

        if v not in visit:
            visit.append(v)

        for adjacent in graph[v]:
            if adjacent not in visit:
                Q.append(adjacent)


def solution(n, m, start, info):
    graph = collections.defaultdict(list)
    answer_dfs = []
    answer_bfs = []

    # 양방향 그래프 만들기
    for u, v in info:
        graph[u].append(v)
        graph[v].append(u)

    # 그래프 정렬하기
    for key, value in graph.items():
        graph[key].sort()

    # 탐색
    dfs(start, graph, answer_dfs)
    bfs(start, graph, answer_bfs)

    # 출력
    print(' '.join(map(str, answer_dfs)))
    print(' '.join(map(str, answer_bfs)))


n, m, v = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]

solution(n, m, v, info)
