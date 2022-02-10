import collections
import heapq


def solution(n, s, a, b, fares):
    graph = collections.defaultdict(list)

    for u, v, w in fares:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # 다익스트라 알고리즘!
    def dijkstra(start):
        # 노드가 1부터 시작함으로 1개를 더 만들어 준다!
        # 초기값은 맥스로 설정
        distance = [float('+inf')] * (n + 1)
        # 자기 자신 거리는 0으로 설정
        distance[start] = 0
        Q = []
        heapq.heappush(Q, (0, start))

        while Q:
            # 큐에서 하나 꺼낸다
            now_distance, node = heapq.heappop(Q)
            if distance[node] < now_distance:
                continue

            # 인접한 노드 방문
            for adjacent, weight in graph[node]:
                # 거리가 짧을경우 거리를 교체한후 큐에 넣어주기
                next_distance = now_distance + weight
                if distance[adjacent] > next_distance:
                    distance[adjacent] = next_distance
                    heapq.heappush(Q, (next_distance, adjacent))

        return distance

    # 모든 노드에 대해서 최단거리를 구해 놓는다
    # 노드는 1 부터 시작임으로 0 번째 인덱스는 빈 배열로 만들기
    dp = [[]] + [dijkstra(i) for i in range(1, n + 1)]
    # 초기값을 맥스로 설정
    answer = float('+inf')

    # S -> i 최단거리, i -> a 최단거리, i -> b 최단거리의 합이 최솟값인 i 를 찾아야 한다
    for i in range(1, n + 1):
        answer = min(answer, dp[i][a] + dp[i][b] + dp[i][s])
    return answer


print(solution(6, 4, 6, 2,
               [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                [1, 6, 25]]))
