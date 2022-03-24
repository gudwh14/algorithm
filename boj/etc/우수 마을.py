import sys

sys.setrecursionlimit(10 ** 9)


def solution(N, people, graph):
    visit = [False] * (N + 1)
    dp = [[0, 0] for _ in range(N + 1)]

    def dfs(vertex):
        visit[vertex] = True
        dp[vertex][1] = people[vertex - 1]

        for adjacent in graph[vertex]:
            if not visit[adjacent]:
                dfs(adjacent)
                dp[vertex][0] += max(dp[adjacent][0], dp[adjacent][1])
                dp[vertex][1] += dp[adjacent][0]
                print(dp)

    dfs(1)
    return max(dp[1])


N = int(input())
people = list(map(int, input().split()))
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
print(solution(N, people, graph))
