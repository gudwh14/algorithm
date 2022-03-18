def solution(N, M, infos):
    answer = 0
    infos.sort(key=lambda x: x[2])
    parent = {}

    # 부모 처음 초기화
    for i in range(1, N + 1):
        parent[i] = i

    # FIND 함수
    def find_parent(v):
        # 부모노드가 존재하면 부모 찾기
        if v != parent[v]:
            parent[v] = find_parent(parent[v])
        return parent[v]

    # UNION 함수
    def union(u, v):
        parent_u = find_parent(u)
        parent_v = find_parent(v)

        # 사이클을 형성하지 않으면 해당 간선 추가
        # 부모가 같으면 사이클을 형성하는 것!
        if parent_v != parent_u:
            if u < v:
                parent[parent_v] = parent_u
            else:
                parent[parent_u] = parent_v
            return True
        else:
            return False

    new_info = []
    for u, v, w in infos:
        if union(u, v):
            answer += w
            new_info.append((u, v, w))

    return answer - new_info[-1][-1]


N, M = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, infos))
