def solution(N, infos):
    answer = 0
    edge = 0
    parent = {}
    infos.sort(key=lambda x: x[2])
    for vertex in range(1, N + 1):
        parent[vertex] = vertex
    print(parent)
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

    for u, v, w in infos:
        if edge == N - 1:
            break
        if union(u, v):
            answer += w
            edge += 1
    print(parent)
    return answer


N = int(input())
M = int(input())
infos = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, infos))
