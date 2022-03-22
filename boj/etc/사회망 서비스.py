import sys

sys.setrecursionlimit(10 ** 9)


def solution(N, graph):
    visit = [False] * (N + 1)
    dp = [[0, 0] for _ in range(N + 1)]

    def dfs(vertex):
        visit[vertex] = True
        # 정점에 방문 했을때, 해당 정점이 얼리어답터일때 서브 트리에서 얼리어답터 정점의 개수는 최소 1개 이상이므로, 1로 초기화
        dp[vertex][0] = 1

        for adjacent in graph[vertex]:
            if not visit[adjacent]:
                dfs(adjacent)
                # 정점이 얼리어답터 일경우, 자식 노드는 얼리어답터 or 아니여도 된다. 그중 최솟값을 가져오기
                dp[vertex][0] += min(dp[adjacent][0], dp[adjacent][1])
                # 정점이 얼리어답터가 아니면, 자식노드는 얼리어답터여야한다
                dp[vertex][1] += dp[adjacent][0]

    dfs(1)
    return min(dp[1][0], dp[1][1])


N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
print(solution(N, graph))
