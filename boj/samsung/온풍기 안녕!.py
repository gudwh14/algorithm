import collections


# 온풍기 작동 함수
def heater_on(heaters, board):
    directions = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]
    for heater in heaters:
        x, y, d = heater
        direction = directions[d]
        Q = collections.deque()
        visit = [[False for _ in range(C)] for _ in range(R)]
        visit[x + direction[0]][y + direction[1]] = True
        Q.append((x + direction[0], y + direction[1], 4))
        board[x + direction[0]][y + direction[1]] += 5

        # 5, 4, 3, 2, 1 반복
        while Q:
            r, c, value = Q.popleft()

            if d == 1:
                for idx in [-1, 0, 1]:
                    new_r = r + idx
                    new_c = c + direction[1]

                    if 0 <= new_r < R and 0 <= new_c < C and not visit[new_r][new_c]:
                        if idx == -1:
                            if horizon_walls[new_r][new_c - 1] or vertical_walls[new_r + 1][new_c - 1]:
                                continue
                        if idx == 0:
                            if horizon_walls[new_r][new_c - 1]:
                                continue
                        if idx == 1:
                            if horizon_walls[new_r][new_c - 1] or vertical_walls[new_r][new_c - 1]:
                                continue
                        board[new_r][new_c] += value
                        visit[new_r][new_c] = True
                        if value - 1 > 0:
                            Q.append((new_r, new_c, value - 1))
            elif d == 2:
                for idx in [-1, 0, 1]:
                    new_r = r + idx
                    new_c = c + direction[1]

                    if 0 <= new_r < R and 0 <= new_c < C and not visit[new_r][new_c]:
                        if idx == -1:
                            if horizon_walls[new_r][new_c] or vertical_walls[new_r + 1][new_c + 1]:
                                continue
                        if idx == 0:
                            if horizon_walls[new_r][new_c]:
                                continue
                        if idx == 1:
                            if horizon_walls[new_r][new_c] or vertical_walls[new_r][new_c + 1]:
                                continue
                        board[new_r][new_c] += value
                        visit[new_r][new_c] = True
                        if value - 1 > 0:
                            Q.append((new_r, new_c, value - 1))
            elif d == 3:
                for idx in [-1, 0, 1]:
                    new_r = r + direction[0]
                    new_c = c + idx

                    if 0 <= new_r < R and 0 <= new_c < C and not visit[new_r][new_c]:
                        if idx == -1:
                            if vertical_walls[new_r + 1][new_c] or horizon_walls[new_r + 1][new_c]:
                                continue
                        if idx == 0:
                            if vertical_walls[new_r + 1][new_c]:
                                continue
                        if idx == 1:
                            if vertical_walls[new_r + 1][new_c] or horizon_walls[new_r + 1][new_c - 1]:
                                continue
                        board[new_r][new_c] += value
                        visit[new_r][new_c] = True
                        if value - 1 > 0:
                            Q.append((new_r, new_c, value - 1))
            elif d == 4:
                for idx in [-1, 0, 1]:
                    new_r = r + direction[0]
                    new_c = c + idx

                    if 0 <= new_r < R and 0 <= new_c < C and not visit[new_r][new_c]:
                        if idx == -1:
                            if vertical_walls[new_r][new_c] or horizon_walls[new_r - 1][new_c]:
                                continue
                        if idx == 0:
                            if vertical_walls[new_r][new_c]:
                                continue
                        if idx == 1:
                            if vertical_walls[new_r][new_c] or horizon_walls[new_r - 1][new_c - 1]:
                                continue
                        board[new_r][new_c] += value
                        visit[new_r][new_c] = True
                        if value - 1 > 0:
                            Q.append((new_r, new_c, value - 1))


# 온도 이동
def move_temper(board):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                temper = board[i][j]
                for idx in range(4):
                    new_i = i + directions[idx][0]
                    new_j = j + directions[idx][1]
                    if 0 <= new_i < R and 0 <= new_j < C and temper > board[new_i][new_j]:
                        if idx == 0:
                            if vertical_walls[i][j]:
                                continue
                        if idx == 1:
                            if horizon_walls[i][j]:
                                continue
                        if idx == 2:
                            if vertical_walls[i + 1][j]:
                                continue
                        if idx == 3:
                            if horizon_walls[i][j - 1]:
                                continue
                        adjacent = board[new_i][new_j]
                        diff = (temper - adjacent) // 4
                        if temper > adjacent:
                            temp[i][j] -= diff
                            temp[new_i][new_j] += diff

    for i in range(R):
        for j in range(C):
            board[i][j] += temp[i][j]


# 가장자리 감소
def set_temper(board, edges):
    for edge in edges:
        r, c = edge
        if board[r][c] > 0:
            board[r][c] -= 1


# 체크 함수
def check_K(board, checks):
    count = 0
    n = len(checks)

    for check in checks:
        r, c = check
        if board[r][c] >= K:
            count += 1

    if count == n:
        return True
    return False


def solution(board):
    answer = 0
    checks = []
    heaters = []
    edges = []
    # 초기 설정 ( 온풍기 위치, 엣지 위치, 체크 위치 설정 )
    for i in range(R):
        for j in range(C):
            if board[i][j] == 5:
                checks.append((i, j))
            elif board[i][j] > 0:
                heaters.append((i, j, board[i][j]))

            if i == 0 or j == 0 or i == R - 1 or j == C - 1:
                edges.append((i, j))
            board[i][j] = 0
    while True:
        heater_on(heaters, board)
        move_temper(board)
        set_temper(board, edges)
        answer += 1
        if answer > 100:
            return 101
        if check_K(board, checks):
            break
    return answer


R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
W = int(input())
walls = [list(map(int, input().split())) for _ in range(W)]
vertical_walls = [[False for _ in range(C)] for _ in range(R)]
horizon_walls = [[False for _ in range(C)] for _ in range(R)]
# 벽 위치 저장하기
for wall in walls:
    x, y, t = wall
    if t == 0:
        vertical_walls[x - 1][y - 1] = True
    if t == 1:
        horizon_walls[x - 1][y - 1] = True
print(solution(board))
