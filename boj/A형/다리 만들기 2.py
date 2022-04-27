# 섬의 정보를 찾는 함수
# dfs 로 섬 구하기
def find_island(board):
    # 섬들의 좌표를 저장하는 변수
    islands = []
    visit = [[False] * M for _ in range(N)]
    # 해당 섬의 좌표가 몇번 섬에 속하는지 저장하는 변수
    info = [[-1] * M for _ in range(N)]
    # 섬 카운팅
    count = 0

    def dfs(r, c, island):
        visit[r][c] = True
        info[r][c] = count
        island.append((r, c))

        for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = r + direct[0]
            new_c = c + direct[1]

            if 0 <= new_r < N and 0 <= new_c < M and board[new_r][new_c] == 1 and not visit[new_r][new_c]:
                dfs(new_r, new_c, island)

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and not visit[i][j]:
                island = []
                dfs(i, j, island)
                islands.append(island)
                count += 1

    return islands, info


def calc_min_distance(islands, info):
    n = len(islands)
    distances = [[float('+inf')] * n for _ in range(n)]

    # 해당 섬에서 다른 섬까지의 최단거리 구하기
    # 다리는 가로로만 or 세로로만 놓을 수 있다!
    for idx, island in enumerate(islands):
        for r, c in island:
            temp = []
            # 상
            for i in range(1, N):
                new_r = r - i
                if 0 <= new_r < N:
                    if board[new_r][c] == 1:
                        temp.append((new_r, c))
                        break
                else:
                    break
            # 하
            for i in range(1, N):
                new_r = r + i
                if 0 <= new_r < N:
                    if board[new_r][c] == 1:
                        temp.append((new_r, c))
                        break
                else:
                    break
            # 좌
            for j in range(1, M):
                new_c = c - j
                if 0 <= new_c < M:
                    if board[r][new_c] == 1:
                        temp.append((r, new_c))
                        break
                else:
                    break
            # 우
            for j in range(1, M):
                new_c = c + j
                if 0 <= new_c < M:
                    if board[r][new_c] == 1:
                        temp.append((r, new_c))
                        break
                else:
                    break
            for i, j in temp:
                if info[i][j] != idx and info[i][j] >= 0:
                    distance = abs(r - i) + abs(c - j) - 1
                    if distance > 1:
                        distances[idx][info[i][j]] = min(distances[idx][info[i][j]], distance)
    return distances


# 최단거리를 기반으로 간선 정보 구하기
def make_edges(distances):
    edges = []
    n = len(distances)

    for i in range(n):
        for j in range(n):
            if distances[i][j] != float('+inf'):
                edges.append((i, j, distances[i][j]))

    return edges


def solution(board):
    answer = 0
    count = 0
    islands, info = find_island(board)
    distances = calc_min_distance(islands, info)
    edges = make_edges(distances)

    # 크루스칼 알고리즘 진행
    n = len(distances)
    # 간선 가중치를 기준으로 오름차순으로 정렬
    edges.sort(key=lambda x: x[2])

    # parent
    parent = [p for p in range(n)]

    # find
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    # union 함수
    def union(a, b):
        parent_a = find(a)
        parent_b = find(b)

        if parent_a != parent_b:
            if a < b:
                parent[parent_b] = parent_a
            else:
                parent[parent_a] = parent_b
            return True
        else:
            return False

    for u, v, w in edges:
        if count == n - 1:
            break
        if union(u, v):
            answer += w
            count += 1

    # 만약 모든 섬이 연결되지 않는다면 -1 반환
    if count != n - 1:
        return -1
    return answer


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(board))
