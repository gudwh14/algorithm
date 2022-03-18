import collections


def solution(N, infos):
    graph = collections.defaultdict(list)
    in_degree = [0 for _ in range(N + 1)]
    in_degree[0] = -1
    # 해당 건물을 짓는데 걸리는 시간을 저장하는 변수
    times = [0]
    # 해당 건물을 짓는데 걸리는 총 시간(이전 건물 짓는 시간 포함)을 저장하는 변수
    distances = [0 for _ in range(N + 1)]

    # 그래프 구하기 및 in_degree 구하기
    for u in range(N):
        w = infos[u][0]
        times.append(w)
        for i in range(1, len(infos[u]) - 1):
            graph[infos[u][i]].append(u + 1)
            in_degree[u + 1] += 1

    # in_degree가 0인 애들을 시작 정점으로설정
    starts = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            starts.append(i)
            distances[i] = times[i]

    visit = [False for _ in range(N + 1)]

    for start in starts:
        Q = collections.deque()
        Q.append(start)
        visit[start] = True

        while Q:
            vertex = Q.popleft()

            for adjacent in graph[vertex]:
                if not visit[adjacent]:
                    in_degree[adjacent] -= 1
                    if in_degree[adjacent] <= 0:
                        visit[adjacent] = True
                        Q.append(adjacent)
                    # 해당 건물을 짓는 총 시간은 = max(해당 건물을 짓는 총 시간, 현재 건물을 짓는 총시간 + 해당 건물을 짓는 시간)
                    distances[adjacent] = max(distances[adjacent], distances[vertex] + times[adjacent])

    for i in range(1, N + 1):
        print(distances[i])


N = int(input())
infos = [list(map(int, input().split())) for _ in range(N)]
solution(N, infos)
