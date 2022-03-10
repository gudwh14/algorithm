import collections


# 위상정렬을 사용하는 문제
def solution(N, M, infos):
    answer = []
    in_degree = [0 for _ in range(N + 1)]
    graph = collections.defaultdict(list)

    # 그래프 설정과, InDegree 구하기
    for u, v in infos:
        graph[u].append(v)
        in_degree[v] += 1

    # 0번 정점은 -1로 설정
    in_degree[0] = -1
    visit = [False for _ in range(N + 1)]

    starts = []
    # InDegree가 0인 정점 구하기
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            starts.append(i)

    # InDegree가 0인 정점 부터 위상정렬 시작
    for start in starts:
        Q = collections.deque()
        Q.append(start)
        visit[start] = True
        answer.append(start)

        while Q:
            vertex = Q.popleft()

            for adjacent in graph[vertex]:
                # 방문하지 않은 정점이면
                if not visit[adjacent]:
                    # InDegree 감소
                    in_degree[adjacent] -= 1
                    # InDegree가 0이 되면 큐에 넣어주기
                    if in_degree[adjacent] == 0:
                        Q.append(adjacent)
                        visit[adjacent] = True
                        answer.append(adjacent)

    for v in answer:
        print(v, end=' ')


N, M = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, infos)
