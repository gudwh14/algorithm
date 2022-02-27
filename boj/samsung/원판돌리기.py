def print_board(board):
    for bo in board:
        print(bo)
    print()

# 시계 방향으로 회전하는함수
def turn_right(M, board, idx, K):
    temp = None
    next_temp = None

    # K번 만큼 회전
    for _ in range(K):
        for i in range(M):
            if temp == None:
                next_temp = board[idx][i + 1]
                board[idx][i + 1] = board[idx][i]
                temp = next_temp
            else:
                if i == M - 1:
                    next_temp = board[idx][0]
                    board[idx][0] = temp
                    temp = next_temp
                else:
                    next_temp = board[idx][i + 1]
                    board[idx][i + 1] = temp
                    temp = next_temp
        temp = None
        next_temp = None


# 반시계 방향으로 회전하는 함수
def turn_left(M, board, idx, K):
    board = [] + board
    temp = None
    next_temp = None

    for _ in range(K):
        for i in range(M - 1, -1, -1):
            if temp == None:
                next_temp = board[idx][i - 1]
                board[idx][i - 1] = board[idx][i]
                temp = next_temp
            else:
                if i == 0:
                    next_temp = board[idx][M - 1]
                    board[idx][M - 1] = temp
                    temp = next_temp
                else:
                    next_temp = board[idx][i - 1]
                    board[idx][i - 1] = temp
                    temp = next_temp
        temp = None
        next_temp = None

# 인접한 동일한 수 찾아주는 함수
def check_num(N, M, idx, board):
    # 인접한 수의 좌표들을 저장하는 변수
    find = []
    for j in range(M):
        # 같은 원형판 좌, 우 인접 비교
        if board[idx][j] != 0:
            if j == 0:
                if board[idx][0] == board[idx][1]:
                    find.append((idx, 1))
                    find.append((idx, 0))
                if board[idx][0] == board[idx][-1]:
                    find.append((idx, M - 1))
                    find.append((idx, 0))
            elif j == M - 1:
                if board[idx][j] == board[idx][M - 2]:
                    find.append((idx, M - 2))
                    find.append((idx, j))
                if board[idx][j] == board[idx][0]:
                    find.append((idx, 0))
                    find.append((idx, j))
            elif 1 <= j < M - 1:
                if board[idx][j] == board[idx][j - 1]:
                    find.append((idx, j - 1))
                    find.append((idx, j))
                if board[idx][j] == board[idx][j + 1]:
                    find.append((idx, j + 1))
                    find.append((idx, j))

            # 반지름이 다른 원형칸의 상, 하 비교
            if idx == 0:
                if board[idx][j] == board[idx + 1][j]:
                    find.append((idx + 1, j))
                    find.append((idx, j))
            elif idx == N - 1:
                if board[idx][j] == board[idx - 1][j]:
                    find.append((idx - 1, j))
                    find.append((idx, j))
            elif 1 <= idx <= N - 2:
                if board[idx][j] == board[idx + 1][j]:
                    find.append((idx + 1, j))
                    find.append((idx, j))
                if board[idx][j] == board[idx - 1][j]:
                    find.append((idx - 1, j))
                    find.append((idx, j))

    return find

# 인접한 수를 못찾았을때 실행하는 함수
def no_find(N, M, board, avg, total_sum):
    for i in range(N):
        for j in range(M):
            # 평균 값 보다 크면 -1, 작으면 +1
            if board[i][j] > avg:
                board[i][j] -= 1
                total_sum -= 1
            elif 0 < board[i][j] < avg:
                board[i][j] += 1
                total_sum += 1

    return total_sum


def calc_board(N, M, board):
    result = 0
    for i in range(N):
        for j in range(M):
            result += board[i][j]
    return result


def solution(N, M, board, commands):
    # N번째 원판에 존재하는 숫자의 개수를 담아두는 배열
    board_info = [M for _ in range(N)]
    # 원판의 총 수의 합
    total_sum = calc_board(N, M, board)
    # 원판의 수의 총 개수
    total = sum(board_info)

    for command in commands:
        x, d, k = command
        # 원판 회전
        product = 1
        if d == 0:
            while x * product <= N:
                turn_right(M, board, x * product - 1, k % M)
                product += 1
        elif d == 1:
            while x * product <= N:
                turn_left(M, board, x * product - 1, k % M)
                product += 1

        find = []
        for idx in range(N):
            if board_info[idx] > 0:
                find += check_num(N, M, idx, board)
        # 인접한 수 가 있으면 제거
        if find:
            for i, j in set(find):
                total_sum -= board[i][j]
                board[i][j] = 0
                board_info[i] -= 1
                total -= 1
        else:
            if total == 0:
                return 0
            avg = total_sum / total
            total_sum = no_find(N, M, board, avg, total_sum)
    return total_sum


N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(T)]
print(solution(N, M, board, commands))
