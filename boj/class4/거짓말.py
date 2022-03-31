import collections

# union & find 로 해결가능
def solution(N, M, truths, partys):
    answer = 0
    status = collections.defaultdict(int)

    if len(truths) == 1:
        return M
    truths = truths[1:]
    graph = collections.defaultdict(list)

    for party in partys:
        for i in range(len(party) - 1):
            graph[party[i]].append(party[i + 1])
            graph[party[i + 1]].append(party[i])

    visit = [False] * (N + 1)

    def dfs(vertex):
        visit[vertex] = True
        status[vertex] = 1
        truths.append(vertex)

        for adjacent in graph[vertex]:
            if not visit[adjacent]:
                dfs(adjacent)

    for node in truths:
        if not visit[node]:
            dfs(node)

    for party in partys:
        for man in party:
            if status[man] == 1:
                break
        else:
            answer += 1
    return answer


N, M = map(int, input().split())
truths = list(map(int, input().split()))
partys = [list(map(int, input().split()))[1:] for _ in range(M)]
print(solution(N, M, truths, partys))
