import collections


def solution(N, S):
    answer = 0
    graph = collections.defaultdict(list)
    visit = [False] * (N + 1)

    for i in range(N):
        graph[i + 1].append(S[i])

    def dfs(vertex):
        visit[vertex] = True

        for adjacent in graph[vertex]:
            if not visit[adjacent]:
                dfs(adjacent)

    for i in range(1, N + 1):
        if not visit[i]:
            dfs(i)
            answer += 1

    print(answer)


T = int(input().split()[0])
for _ in range(T):
    N = int(input().split()[0])
    S = list(map(int, input().split()))
    solution(N, S)
