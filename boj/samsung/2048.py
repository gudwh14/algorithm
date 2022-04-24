import collections

# 상, 하, 좌, 우 이동 로직
def right(n, board):
    # 해당 칸이 이미 합쳐진 칸인지 판단하는 변수
    visit = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n - 1, -1, -1):
            index = j
            # 숫자를 발견하면 이동 시작
            if board[i][j] != 0:
                while index < n - 1:
                    # 이동하려는 칸이 0 이거나, 자기 자신과 같다면 이동 하여 합쳐줌
                    # 이미 합쳐진 칸에는 합쳐지지 않아야 함으로, 현재 칸과 이동하려는 칸이 visit 배열에 존재하는지 체크
                    if board[i][index + 1] == 0 or (board[i][index + 1] == board[i][index] and not visit[i][index + 1] and not visit[i][index]):
                        # 숫자가 합쳐지는 경우에만, visit 배열에 합쳐진칸 좌표 저장
                        if board[i][index + 1] == board[i][index]:
                            visit[i][index + 1] = True
                        board[i][index + 1] += board[i][index]
                        board[i][index] = 0
                    index += 1
    return board


def left(n, board):
    visit = [[False for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(0, n):
            index = j
            if board[i][j] != 0:
                while index > 0:
                    if board[i][index - 1] == 0 or (board[i][index - 1] == board[i][index] and not visit[i][index - 1] and not visit[i][index]):
                        if board[i][index - 1] == board[i][index]:
                            visit[i][index - 1] = True
                        board[i][index - 1] += board[i][index]
                        board[i][index] = 0
                    index -= 1
    return board


def up(n, board):
    visit = [[False for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(0, n):
            index = i
            if board[i][j] != 0:
                while index > 0:
                    if board[index - 1][j] == 0 or (board[index - 1][j] == board[index][j] and not visit[index- 1][j] and not visit[index][j]):
                        if board[index - 1][j] == board[index][j]:
                            visit[index - 1][j] = True
                        board[index - 1][j] += board[index][j]
                        board[index][j] = 0
                    index -= 1
    return board


def down(n, board):
    visit = [[False for _ in range(n)] for _ in range(n)]

    for j in range(n):
        for i in range(n - 1, -1, -1):
            index = i
            if board[i][j] != 0:
                while index < n - 1:
                    if board[index + 1][j] == 0 or (board[index + 1][j] == board[index][j] and not visit[index + 1][j] and not visit[index][j]):
                        if board[index + 1][j] == board[index][j]:
                            visit[index + 1][j] = True
                        board[index + 1][j] += board[index][j]
                        board[index][j] = 0
                    index += 1
    return board

# 보드의 최대값을 계산하는 함수
def calc_max_number(board):
    _max = -1
    for i in range(len(board)):
        for j in range(len(board)):
            _max = max(_max, board[i][j])

    return _max


def solution(n, board):
    answer = -1
    Q = collections.deque()
    # 초기값은 원래 기존 보드와, 횟수는 0
    Q.append([board, 0])

    while Q:
        # 값 꺼내오기
        board, times = Q.popleft()

        # 횟수가 5번일 경우 종료 및 해당 보드의 최대값 구하기
        if times == 5:
            answer = max(answer, calc_max_number(board))
            continue

        # 상, 하, 좌, 우로 이동
        up_board = [item[:] for item in board]
        down_board = [item[:] for item in board]
        left_board = [item[:] for item in board]
        right_board = [item[:] for item in board]
        Q.append([up(n, up_board), times + 1])
        Q.append([left(n, left_board), times + 1])
        Q.append([right(n, right_board), times + 1])
        Q.append([down(n, down_board), times + 1])

    return answer


n = int(input().split()[0])
board = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, board))
