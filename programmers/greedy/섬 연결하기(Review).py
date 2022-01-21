# 크루스칼 알고리즘
# 탐욕법을 이용하여 모든정점을 최소비용으로 연결하여 최적 해답을 구하는것!
# 그래프의 간선들을 가중치의 오름차순으로 정렬한다.
# 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택한다.
# 즉, 가장 낮은 가중치를 먼저 선택한다.
# 사이클을 형성하는 간선을 제외한다.
# 해당 간선을 현재의 MST(최소 비용 신장 트리)의 집합에 추가한다.
def solution(n, costs):
    # kruskal algorithm
    ans = 0
    costs.sort(key=lambda x: x[2])  # cost 기준으로 오름차순 정렬
    routes = set([costs[0][0]])  # 집합
    print(costs)
    while len(routes) != n:
        for i, cost in enumerate(costs):
            # 사이클이 존재하면 스킵
            if cost[0] in routes and cost[1] in routes:
                continue
            # 존재하지 않으면 set에 추가
            if cost[0] in routes or cost[1] in routes:
                # update : 여러개 추가하기
                routes.update([cost[0], cost[1]])
                print(routes)
                ans += cost[2]
                costs[i] = [-1, -1, -1]
                break
    return ans


print(solution(4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))
