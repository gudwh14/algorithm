import collections

# 주사위 굴리기
def roll_dice(direction, dice, coordinate):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    r, c = coordinate
    new_r = r + directions[direction][0]
    new_c = c + directions[direction][1]

    # 만약 이동 할수 없으면 주사위 이동방향 반대로 바꾸기
    if not (0 <= new_r < N and 0 <= new_c < M):
        direction = (direction + 2) % 4
        new_r = r + directions[direction][0]
        new_c = c + directions[direction][1]

    # 각 면에 존재하는 기존값 저장하기
    top = dice[1][1]
    right = dice[1][2]
    left = dice[1][0]
    bottom = dice[3][1]
    up = dice[0][1]
    down = dice[2][1]
    # direction 동, 남, 서, 북
    if direction == 0:
        dice[1][2] = top
        dice[1][1] = left
        dice[1][0] = bottom
        dice[3][1] = right
    elif direction == 1:
        dice[2][1] = top
        dice[3][1] = down
        dice[1][1] = up
        dice[0][1] = bottom
    elif direction == 2:
        dice[1][2] = bottom
        dice[1][1] = right
        dice[1][0] = top
        dice[3][1] = left
    elif direction == 3:
        dice[2][1] = bottom
        dice[3][1] = up
        dice[1][1] = down
        dice[0][1] = top
    return direction, (new_r, new_c)


def calc_score(board, coordinate):
    r, c = coordinate
    B = board[r][c]
    visit = [[False for _ in range(M)] for _ in range(N)]
    Q = collections.deque()
    Q.append((r, c))
    visit[r][c] = True
    count = 0

    while Q:
        r, c = Q.popleft()
        count += 1

        for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = r + direct[0]
            new_c = c + direct[1]

            if 0 <= new_r < N and 0 <= new_c < M and board[new_r][new_c] == B and not visit[new_r][new_c]:
                Q.append((new_r, new_c))
                visit[new_r][new_c] = True

    return count * B


def calc_direct(board, dice, coordinate, direction):
    bottom = dice[3][1]
    r, c = coordinate
    B = board[r][c]

    if bottom > B:
        direction = (direction + 1) % 4
    elif bottom < B:
        direction -= 1
        if direction < 0:
            direction = 3
    elif bottom == B:
        pass
    return direction


def solution(board):
    answer = 0
    # 초기 주사위
    dice = [[0, 2, 0], [4, 1, 3], [0, 5, 0], [0, 6, 0]]
    # 초기 이동 방향
    direction = 0
    # 초기 좌표
    coordinate = (0, 0)
    for _ in range(K):
        # 주사위 굴리기
        direction, coordinate = roll_dice(direction, dice, coordinate)
        # 점수 계산
        answer += calc_score(board, coordinate)
        # 이동방향 결정하기
        direction = calc_direct(board, dice, coordinate, direction)

    return answer


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(board))
