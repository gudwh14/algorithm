import collections


def solution(n, m, info):
    answer = 0
    graph = collections.defaultdict(list)

    # 무방향(양방향) 그래프
    for u, v in info:
        graph[u].append(v)
        graph[v].append(u)

    visit = []

    def dfs(vertex):
        visit.append(vertex)

        for adjacent in graph[vertex]:
            # 중첩 방문 방지
            if adjacent not in visit:
                dfs(adjacent)

    # 정점이 1 부터 N 까지 이므로 범위설정을 잘해야함!
    for i in range(1, n + 1):
        # 방문하지 않은 정점이면 dfs 탐색 시작
        if i not in visit:
            dfs(i)
            # 카운트 증가
            answer += 1

    return answer


n, m = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, info))
