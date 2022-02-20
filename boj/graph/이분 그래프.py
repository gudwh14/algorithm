import collections
import sys

sys.setrecursionlimit(10 ** 6)


def solution(V, E, info):
    visit = [0] * (V + 1)
    graph = collections.defaultdict(list)

    # 무방향 그래프
    for u, v in info:
        graph[u].append(v)
        graph[v].append(u)

    # 처음 들어온 정점을 1로, 인근 정점을 -1로 색칠
    def dfs(vertex, group):
        visit[vertex] = group

        for adjacent in graph[vertex]:
            # 방문하지 않을 정점 방문
            if visit[adjacent] == 0:
                # 이분그래프가 아니면 FALSE
                if not dfs(adjacent, -group):
                    return False
            # 방문한 정점일경우, 현재 정점색과 방문할 인근 정점색이 같으면 이분 그래프가 아니다
            elif visit[adjacent] == visit[vertex]:
                return False

        return True

    flag = True
    for i in range(1, V + 1):
        if visit[i] == 0:
            flag = dfs(i, 1)
            if not flag:
                break

    if flag:
        print('YES')
    else:
        print('NO')


k = int(input().split()[0])
for _ in range(k):
    V, E = map(int, input().split())
    info = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
    solution(V, E, info)
