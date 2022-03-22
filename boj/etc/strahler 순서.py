import collections


def solution(K, M, P, infos):
    graph = collections.defaultdict(list)
    orders = [0 for _ in range(M + 1)]
    in_degree = [0 for _ in range(M + 1)]

    for u, v in infos:
        graph[u].append(v)
        in_degree[v] += 1

    starts = []
    visit = [False] * (M + 1)
    in_order = [[] for _ in range(M + 1)]

    for i in range(1, M + 1):
        if in_degree[i] == 0:
            orders[i] = 1
            starts.append(i)
            visit[i] = True

    for start in starts:
        Q = collections.deque()
        Q.append(start)

        while Q:
            vertex = Q.popleft()

            for adjacent in graph[vertex]:
                if not visit[adjacent]:
                    in_degree[adjacent] -= 1
                    in_order[adjacent].append(orders[vertex])
                    if in_degree[adjacent] <= 0:
                        max_order = max(in_order[adjacent])
                        counts = collections.Counter(in_order[adjacent])
                        if counts[max_order] > 1:
                            orders[adjacent] = max_order + 1
                        else:
                            orders[adjacent] = max_order
                        visit[adjacent] = True
                        Q.append(adjacent)
    print(K, orders[M])


T = int(input())
for _ in range(T):
    K, M, P = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(P)]
    solution(K, M, P, infos)
