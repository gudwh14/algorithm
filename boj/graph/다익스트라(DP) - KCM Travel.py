import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


# 다익스트라 알고리즘은 그리디와 같은데, 현재 시간과 비용 두가지를 고려해야 하기 때문에 항상 최선의 선택을 찾을수없다.
# DP를 이용해서 풀이
# 비용에 대한 제한이 있으므로 모든 비용에 대한 상태값을 구하기!!
# 시간 제한 10초!
def solution(N, M, K, infos):
    graph = collections.defaultdict(list)

    for u, v, w, d in infos:
        graph[u].append((v, w, d))

    # 모든 비용에 대해 정점까지의 거리에 대한 테이블 만들기
    dp = [[float('+inf') for _ in range(M + 1)] for _ in range(N + 1)]
    # 시작점 초기화 COST : 0 일때 0
    dp[1][0] = 0

    # 모든 비용 탐색
    for money in range(M + 1):
        # 모든 정점 탐색
        for vertex in range(1, N + 1):
            # 인접 정점 탐색
            for adjacent in graph[vertex]:
                node, cost, time = adjacent

                # 방문할 정점의 비용의 합이 M보다 작을때만
                if money + cost <= M:
                    # 인접정점까지의 시간은 1.현재 인접정점의 시간과, 2. 현재 정점까지의 시간 에서 인접정점까지의 시간의 합중 최솟값 으로 업데이트
                    dp[node][money + cost] = min(dp[node][money + cost], dp[vertex][money] + time)

    dp[N].sort()
    answer = dp[N][0]
    if answer == float('+inf'):
        print('Poor KCM')
    else:
        print(answer)


T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    infos = [list(map(int, input().split())) for _ in range(K)]
    solution(N, M, K, infos)
