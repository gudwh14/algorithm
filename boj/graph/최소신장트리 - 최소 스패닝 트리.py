def solution(V, infos):
    answer = 0
    parent = {}
    # 그리디 방식이므로 가중치를 기준으로 오름차순으로 간선들 정렬
    infos.sort(key=lambda x: x[2])
    for vertex in range(1, V + 1):
        parent[vertex] = vertex

    # Find 함수
    def find_parent(x):
        # 기존 방식
        # if x != parent[x]:
        #     return find_parent(parent[x])
        # return x

        # 압축 경로 방식
        # 미리 부모 노드 값을 갱신 하기
        if x != parent[x]:
            parent[x] = find_parent(parent[x])
        return parent[x]

    # Union 함수
    def union_parent(a, b):
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

    # 크루스칼 알고리즘
    for u, v, w in infos:
        if union_parent(u, v):
            answer += w

    return answer


V, E = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(E)]
print(solution(V, infos))
