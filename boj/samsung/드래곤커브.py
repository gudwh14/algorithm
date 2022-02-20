def print_board(board):
    for bo in board:
        print(bo)
    print()

# 드래곤 커브를 그리는 함수
def draw_dragon(x, y, d, g, board):
    # d 방향에 따른 좌표 증감값을 저장한 변수
    directions = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    # 각 세대의 방향을 저장하는 변수
    stack = []

    for i in range(g + 1):
        # 0세대일 경우, d 방향으로 이동
        if i == 0:
            board[y][x] = 1
            y += directions[d][0]
            x += directions[d][1]
            board[y][x] = 1
            stack.append(d)
        # 1세대 부터, 이전 세대의 방향을 뒤에서 부터 읽어와, 90도 시계방향으로 전환후 이동
        else:
            # 이전 세대 방향 읽기
            for idx in range(len(stack) - 1, -1, -1):
                # 방향
                nd = stack[idx]
                # 90도 전환
                nd = (nd + 1) % 4
                y += directions[nd][0]
                x += directions[nd][1]
                # 이동
                board[y][x] = 1
                # 현재 방향 저장
                stack.append(nd)

# 1 X 1 정사각형 찾는 함수
def find_square(board):
    count = 0
    # (100, 100) 까지 좌표까지만 탐색
    for i in range(100):
        for j in range(100):
            if board[i][j] == 1:
                if board[i + 1][j] == 1 and board[i][j + 1] == 1 and board[i + 1][j + 1] == 1:
                    count += 1

    return count


def solution(n, dragons):
    # 시작 좌표가 (100, 100) 까지 들어오기 때문에, 101 X 101 개의 배열을 만들어준다.
    board = [[0 for _ in range(101)] for _ in range(101)]

    for x, y, d, g in dragons:
        draw_dragon(x, y, d, g, board)

    return find_square(board)


n = int(input().split()[0])
dragons = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, dragons))
