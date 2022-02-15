import sys

# 주사위의 각 면을 가르키는 dice 좌표
top = (1, 1)
bottom = (3, 1)
left = (1, 0)
right = (1, 2)
up = (0, 1)
down = (2, 1)


def print_dice(dice):
    for d in dice:
        print(d)
    print()

# 주사위 굴리기
def roll_dice(cmd, dice):
    # 기존 값 tmp 저장
    tmp_top = dice[top[0]][top[1]]
    tmp_bottom = dice[bottom[0]][bottom[1]]
    tmp_right = dice[right[0]][right[1]]
    tmp_left = dice[left[0]][left[1]]
    tmp_up = dice[up[0]][up[1]]
    tmp_down = dice[down[0]][down[1]]

    # 동쪽으로 굴리기
    if cmd == 1:
        dice[top[0]][top[1]] = tmp_left
        dice[right[0]][right[1]] = tmp_top
        dice[left[0]][left[1]] = tmp_bottom
        dice[bottom[0]][bottom[1]] = tmp_right
    # 서쪽으로 굴리기
    elif cmd == 2:
        dice[top[0]][top[1]] = tmp_right
        dice[right[0]][right[1]] = tmp_bottom
        dice[left[0]][left[1]] = tmp_top
        dice[bottom[0]][bottom[1]] = tmp_left
    # 북쪽으로 굴리기
    elif cmd == 3:
        dice[top[0]][top[1]] = tmp_down
        dice[bottom[0]][bottom[1]] = tmp_up
        dice[up[0]][up[1]] = tmp_top
        dice[down[0]][down[1]] = tmp_bottom
    # 남쪽으로 굴리기
    elif cmd == 4:
        dice[top[0]][top[1]] = tmp_up
        dice[bottom[0]][bottom[1]] = tmp_down
        dice[up[0]][up[1]] = tmp_bottom
        dice[down[0]][down[1]] = tmp_top


def solution(n, m, x, y, k, board, cmds):
    # 주사위 0 으로 초기화
    dice = [[0 for _ in range(3)] for _ in range(4)]
    # 지도 좌표 이동
    directions = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]

    pos = (x, y)

    for cmd in cmds:
        ni, nj = pos
        ni += directions[cmd][0]
        nj += directions[cmd][1]

        # 주사위가 지도에 유요한 위치에 있을경우에만 동작
        if 0 <= ni < n and 0 <= nj < m:
            pos = (ni, nj)
            # 주사위 굴리기
            roll_dice(cmd, dice)
            # 지도의 바닥면이 0일경우
            if board[ni][nj] == 0:
                board[ni][nj] = dice[bottom[0]][bottom[1]]
            # 지도의 바닥면이 0이 아닐경우
            else:
                dice[bottom[0]][bottom[1]] = board[ni][nj]
                board[ni][nj] = 0
            print(dice[top[0]][top[1]])


tmp = list(map(int, sys.stdin.readline().split()))
n = tmp[0]
m = tmp[1]
x = tmp[2]
y = tmp[3]
k = tmp[4]

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
cmds = list(map(int, sys.stdin.readline().split()))

solution(n, m, x, y, k, board, cmds)
