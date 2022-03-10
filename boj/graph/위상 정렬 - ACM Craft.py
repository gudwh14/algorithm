import collections


def solution(N, times, infos, target):
    graph = collections.defaultdict(list)
    in_degree = [0 for _ in range(N + 1)]
    in_degree[0] = -1

    # in 차수 구하기
    for u, v in infos:
        graph[u].append(v)
        in_degree[v] += 1

    # in 차수가 0인 정점 구하기
    starts = []
    for idx in range(1, N + 1):
        if in_degree[idx] == 0:
            starts.append(idx)

    visit = [False for _ in range(N + 1)]
    # 해당 건물을 짓기 위한 선수 건물을 저장하는 변수
    result = [[] for _ in range(N + 1)]
    # 위상정렬 순서를 저장하는 변수
    answer = []

    for start in starts:
        Q = collections.deque()
        Q.append(start)
        visit[start] = True
        answer.append((start, []))

        while Q:
            vertex = Q.popleft()

            for adjacent in graph[vertex]:
                if not visit[adjacent]:
                    in_degree[adjacent] -= 1
                    result[adjacent].append(vertex)
                    if in_degree[adjacent] == 0:
                        Q.append(adjacent)
                        visit[adjacent] = True
                        answer.append((adjacent, result[adjacent]))

    # 해당 건물을 짓는 총 건설시간
    install = [0 for _ in range(N + 1)]
    for vertex, prev in answer:
        # 선행 건물이 없으면, 그냥 해당 건물의 건설 시간만큼 소요
        if not prev:
            install[vertex] = times[vertex - 1]
        # 선행 건물이 있으면, 선행 건물들의 건설시간중 최대값 + 해당 건물 건설시간
        else:
            prev_time = -1
            for prev_vertex in prev:
                prev_time = max(prev_time, install[prev_vertex])
            install[vertex] = times[vertex - 1] + prev_time

        if vertex == target:
            break
    return install[target]


T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    infos = [list(map(int, input().split())) for _ in range(K)]
    target = int(input())
    print(solution(N, times, infos, target))
