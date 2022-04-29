def print_board(board):
    for bo in board:
        print(bo)
    print()


def blizzard(magic, shark, board):
    directions = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
    d, s = magic
    r, c = shark
    for idx in range(1, s + 1):
        new_r = r + directions[d][0] * idx
        new_c = c + directions[d][1] * idx

        if 0 <= new_r < N and 0 <= new_c < N and board[new_r][new_c] > 0:
            board[new_r][new_c] = 0


def calc_value(shark, value):
    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    direct = 0
    idx = 1
    end = False
    r, c = shark
    val = 1

    # 격자의 중심부 부터 좌,하,우,상 방향으로 방향이 변경하면서 칸의 길이가 늘어남
    while True:
        for i in range(1, idx + 1):
            r = r + directions[direct][0]
            c = c + directions[direct][1]
            value[val] = (r, c)
            val += 1
        if end:
            break

        if direct == 1 or direct == 3:
            idx += 1
            if idx == N:
                idx = N - 1
                end = True
        direct = (direct + 1) % 4


def move_ball(value, board):
    empty_start = None
    empty_count = 0
    is_move = False

    # 칸의 값이 1부터 N ** 2 - 1 까지 반복
    for val, coordinate in value.items():
        r, c = coordinate
        if board[r][c] == 0 and not empty_start:
            empty_count += 1
            empty_start = val
        elif board[r][c] == 0 and empty_start:
            empty_count += 1

        try:
            _r, _c = value[val + 1]
            if empty_start and board[_r][_c] > 0:
                for i in range(empty_start, N * N):
                    i_r, i_c = value[i]
                    try:
                        c_r, c_c = value[i + empty_count]
                        change = board[c_r][c_c]
                    except KeyError:
                        change = 0
                    board[i_r][i_c] = change
                empty_start = None
                empty_count = 0
                is_move = True
        except KeyError:
            board[0][0] = 0
    return is_move


def bomb_ball(value, board, answer_count):
    count = 0
    bomb_start = None
    bomb_val = None
    is_bomb = False
    for val, coordinate in value.items():
        r, c = coordinate
        if bomb_val != board[r][c] and count < 4:
            count = 1
            bomb_start = val
            bomb_val = board[r][c]
        elif bomb_val == board[r][c]:
            count += 1
        elif bomb_val != board[r][c] and count >= 4:
            answer_count[bomb_val - 1] += count
            is_bomb = True
            start = bomb_start
            for idx in range(count):
                x, y = value[start + idx]
                board[x][y] = 0
            count = 1
            bomb_start = val
            bomb_val = board[r][c]
    return is_bomb


def change_ball(value, board):
    new_value = []
    count = 0
    ball_value = None

    for val, coordinate in value.items():
        r, c = coordinate
        if not ball_value:
            count = 1
            ball_value = board[r][c]
        elif ball_value == board[r][c]:
            count += 1
        elif ball_value != board[r][c]:
            new_value.append(count)
            new_value.append(ball_value)
            count = 1
            ball_value = board[r][c]

    for val, coordinate in value.items():
        r, c = coordinate
        try:
            board[r][c] = new_value[val - 1]
        except IndexError:
            break


def solution(N, M, board, infos):
    # 마법사 상어의 위치
    shark = (N // 2, N // 2)
    # 격자의 칸마다 적히는 수 구하기
    value = {}
    calc_value(shark, value)
    # 구슬이 파괴된 개수
    answer_count = [0, 0, 0]

    for i in range(M):
        # 블리자드 마법 시전
        blizzard(infos[i], shark, board)
        # 구슬 이동
        move_ball(value, board)

        # 구슬이 더이상 터지지 않을때 까지 터트리기
        while True:
            is_bomb = bomb_ball(value, board, answer_count)
            # 구슬이 더이상 움직이지 않을때 까지 움직이기
            while True:
                is_move = move_ball(value, board)
                if not is_move:
                    break
            if not is_bomb:
                break

        # 구슬 변환
        change_ball(value, board)
    return answer_count[0] + 2 * answer_count[1] + 3 * answer_count[2]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
infos = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, board, infos))
