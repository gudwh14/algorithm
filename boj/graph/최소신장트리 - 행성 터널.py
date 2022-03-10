# 모든 행성간의 거리(간선)을 구하면 시간 초과 및 메모리 초과
def solution(N, infos):
    answer = 0
    parent = {}
    for idx in range(1, N + 1):
        parent[idx] = idx

    def find_parent(x):
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]

    def union(a, b):
        parent_a = find_parent(a)
        parent_b = find_parent(b)

        if parent_a != parent_b:
            if a < b:
                parent[parent_b] = parent_a
            else:
                parent[parent_a] = parent_b
            return True
        else:
            return False

    edges = []
    # 행성간 터널 비용은 두 행성간의 3개의 좌표(x, y, z) 거리중 최솟값이다.
    # 따라서 각 좌표(x, y, z)마다 가장 인접한 행성간의 간선을 구한다.
    # 오름차순으로 정렬하면 i번째 와 i + 1번째가 행성이 가장 가까운 거리이다.

    for idx in range(3):
        infos.sort(key=lambda x: x[idx])
        for i in range(N - 1):
            edges.append([infos[i][-1], infos[i + 1][-1], abs(infos[i][idx] - infos[i + 1][idx])])

    edges.sort(key=lambda x: x[2])

    for u, v, w in edges:
        if union(u, v):
            answer += w

    return answer


N = int(input())
infos = [list(map(int, input().split())) + [i + 1] for i in range(N)]
print(solution(N, infos))
