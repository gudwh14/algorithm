import collections
import copy


def print_board(board):
    for bo in board:
        print(bo)
    print()


# board에 존재하는 cctv들의 좌표와 타입을 반환하는 함수
def check_cctv(n, m, board):
    cctvs = []

    for i in range(n):
        for j in range(m):
            if board[i][j] != 0 and board[i][j] != 6:
                cctvs.append([i, j, board[i][j]])

    return cctvs


# 왼쪽 방향 감시
def watch_left(n, m, i, j, board):
    for idx in range(j - 1, -1, -1):
        if board[i][idx] == 0:
            board[i][idx] = 7
        elif board[i][idx] == 6:
            break
    return board


# 오른쪽 방향 감시
def watch_right(n, m, i, j, board):
    for idx in range(j + 1, m):
        if board[i][idx] == 0:
            board[i][idx] = 7
        elif board[i][idx] == 6:
            break
    return board


# 위쪽 방향 감시
def watch_up(n, m, i, j, board):
    for idx in range(i - 1, -1, -1):
        if board[idx][j] == 0:
            board[idx][j] = 7
        elif board[idx][j] == 6:
            break
    return board


# 아래쪽 방향 감시
def watch_down(n, m, i, j, board):
    for idx in range(i + 1, n):
        if board[idx][j] == 0:
            board[idx][j] = 7
        elif board[idx][j] == 6:
            break
    return board


# 사각지대 개수 계산해주는 함수
def calc_empty(n, m, board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                count += 1
    return count


def solution(n, m, board):
    answer = []
    cctvs = check_cctv(n, m, board)
    # cctvs 배열에 마지막 값 체크용 추가
    cctvs.append([-1, -1, -1])
    Q = collections.deque()
    # Q 초기값 -> 첫번째 cctv
    i, j, cctv = cctvs[0]
    Q.append((i, j, cctv, 0, board))

    while Q:
        ni, nj, cctv, count, board = Q.popleft()

        # 카운트가 cctv의 개수랑 같아지면 감시 종료
        if count == len(cctvs) - 1:
            answer.append(calc_empty(n, m, board))
            continue

        # 다음에 감시할 cctv 가져오기
        next_i, next_j, next_cctv = cctvs[count + 1]

        # cctv 타입에 따른 감시
        # 1일경우 상, 하, 좌, 우 를 따로따로 감시
        if cctv == 1:
            Q.append((next_i, next_j, next_cctv, count + 1, watch_right(n, m, ni, nj, copy.deepcopy(board))))
            Q.append((next_i, next_j, next_cctv, count + 1, watch_left(n, m, ni, nj, copy.deepcopy(board))))
            Q.append((next_i, next_j, next_cctv, count + 1, watch_up(n, m, ni, nj, copy.deepcopy(board))))
            Q.append((next_i, next_j, next_cctv, count + 1, watch_down(n, m, ni, nj, copy.deepcopy(board))))

        # 2일 경우 2가지 경우가 존재
        if cctv == 2:
            _board = copy.deepcopy(board)
            watch_left(n, m, ni, nj, _board)
            watch_right(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

            _board = copy.deepcopy(board)
            watch_up(n, m, ni, nj, _board)
            watch_down(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

        # 3일 경우 4가지 경우가 존재
        if cctv == 3:
            _board = copy.deepcopy(board)
            watch_up(n, m, ni, nj, _board)
            watch_right(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

            _board = copy.deepcopy(board)
            watch_down(n, m, ni, nj, _board)
            watch_right(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

            _board = copy.deepcopy(board)
            watch_down(n, m, ni, nj, _board)
            watch_left(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

            _board = copy.deepcopy(board)
            watch_left(n, m, ni, nj, _board)
            watch_up(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

        # 4일 경우 4가지 경우가 존재
        if cctv == 4:
            _board = copy.deepcopy(board)
            watch_up(n, m, ni, nj, _board)
            watch_right(n, m, ni, nj, _board)
            watch_left(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

            _board = copy.deepcopy(board)
            watch_up(n, m, ni, nj, _board)
            watch_right(n, m, ni, nj, _board)
            watch_down(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

            _board = copy.deepcopy(board)
            watch_down(n, m, ni, nj, _board)
            watch_right(n, m, ni, nj, _board)
            watch_left(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

            _board = copy.deepcopy(board)
            watch_up(n, m, ni, nj, _board)
            watch_down(n, m, ni, nj, _board)
            watch_left(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

        # 5일 경우 1가지 경우가 존재
        if cctv == 5:
            _board = copy.deepcopy(board)
            watch_up(n, m, ni, nj, _board)
            watch_down(n, m, ni, nj, _board)
            watch_right(n, m, ni, nj, _board)
            watch_left(n, m, ni, nj, _board)
            Q.append((next_i, next_j, next_cctv, count + 1, _board))

    # 오름차순 정렬
    answer.sort()
    # 최솟값 반환
    return answer[0]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, board))
