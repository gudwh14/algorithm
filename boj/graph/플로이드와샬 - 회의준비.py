import collections
import heapq


def dijkstra(start, graph, distances):
    distances[start] = 0
    Q = []
    heapq.heappush(Q, (0, start))

    while Q:
        distance, vertex = heapq.heappop(Q)

        if distances[vertex] < distance:
            continue

        for node in graph[vertex]:
            new_distance = 1 + distance
            if distances[node] > new_distance:
                distances[node] = new_distance
                heapq.heappush(Q, (new_distance, node))

    return distances


def solution(N, infos):
    graph = collections.defaultdict(list)
    INF = float('+inf')
    answer = []

    # 그래프 초기화
    for u, v in infos:
        graph[u].append(v)
        graph[v].append(u)

    groups = []

    def bfs(start):
        visit[start] = True
        group = []
        group.append(start)
        Q = collections.deque()
        Q.append(start)

        while Q:
            vertex = Q.popleft()

            for adjacent in graph[vertex]:
                if not visit[adjacent]:
                    Q.append(adjacent)
                    group.append(adjacent)
                    visit[adjacent] = True

        return group

    visit = [False for _ in range(N + 1)]

    # 각각의 그룹 만들기
    for vertex in range(1, N + 1):
        if not visit[vertex]:
            groups.append(bfs(vertex))

    # 그룹 개수 출력
    print(len(groups))

    # 그룹에서 대표 뽑기
    for group in groups:
        result = []
        distances = [INF for _ in range(N + 1)]
        distances[0] = 0
        for idx in range(1, N + 1):
            if idx not in group:
                distances[idx] = 0
        # 그룹안에서 사람마다 거리 구하기
        for vertex in group:
            distance = dijkstra(vertex, graph, distances[:])
            # 전달되는 최대거리는 max거리
            result.append([vertex, max(distance)])
        # 최솟값의 거리를 가진사람이 대표
        result.sort(key=lambda x: x[1])
        # 대표목록에 추가
        answer.append(result[0][0])

    # 오름차순 정렬
    answer.sort()
    for leader in answer:
        print(leader)


N = int(input())
M = int(input())

infos = [list(map(int, input().split())) for _ in range(M)]
solution(N, infos)
