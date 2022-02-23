def print_board(board):
    for bo in board:
        print(bo)
    print()


# 공기청정기 좌표를 반환해주는 함수
def find_air(R, A):
    up = None
    down = None
    for i in range(R):
        if A[i][0] == -1:
            if not up:
                up = (i, 0)
            else:
                down = (i, 0)
    return up, down


# 미세먼지가 번지는 함수
# 모든 미세먼지가 동시에 번지는 로직
def spread_dust(R, C, A):
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    # 증가값 변수
    increase = [[0] * C for _ in range(R)]
    # 감소값 변수
    decrease = [[0] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if A[i][j] != -1:
                total = 0
                for direct in directions:
                    ni = i + direct[0]
                    nj = j + direct[1]

                    if 0 <= ni < R and 0 <= nj < C and A[ni][nj] > 0:
                        amount = A[ni][nj] // 5
                        total += amount
                        decrease[ni][nj] += amount
                increase[i][j] = total

    for i in range(R):
        for j in range(C):
            A[i][j] += increase[i][j]
            A[i][j] -= decrease[i][j]


# 공기청정기 동작 함수
def air_clean(up, down, R, C, A):
    # 공기청정기 위쪽 방향
    temp = 0

    # 오른쪽으로 밀기
    for j in range(0, C - 1):
        _temp = A[up[0]][j + 1]
        A[up[0]][j + 1] = temp
        temp = _temp

    # 위쪽으로 밀기
    for i in range(up[0], 0, -1):
        _temp = A[i - 1][C - 1]
        A[i - 1][C - 1] = temp
        temp = _temp

    # 왼쪽으로 밀기
    for j in range(C - 1, 0, - 1):
        _temp = A[0][j - 1]
        A[0][j - 1] = temp
        temp = _temp

    # 아래쪽으로 밀기
    for i in range(0, up[0] - 1):
        _temp = A[i + 1][0]
        A[i + 1][0] = temp
        temp = _temp

    # 아래쪽 방향
    temp = 0
    # 오른쪽으로 밀기
    for j in range(0, C - 1):
        _temp = A[down[0]][j + 1]
        A[down[0]][j + 1] = temp
        temp = _temp
    # 아래쪽으로 밀기
    for i in range(down[0], R - 2):
        _temp = A[i + 1][C - 1]
        A[i + 1][C - 1] = temp
        temp = _temp
    # 왼쪽으로 밀기
    for j in range(C, 0, - 1):
        _temp = A[R - 1][j - 1]
        A[R - 1][j - 1] = temp
        temp = _temp
    # 위쪽으로 밀기
    for i in range(R - 1, down[0] + 1, -1):
        _temp = A[i - 1][0]
        A[i - 1][0] = temp
        temp = _temp


# 미세먼지 총량 계산하는 함수
def calc_dust(R, C, A):
    answer = 0
    for i in range(R):
        for j in range(C):
            if A[i][j] > 0:
                answer += A[i][j]

    return answer


def solution(R, C, T, A):
    up, down = find_air(R, A)
    # T만큼 반복
    for _ in range(T):
        spread_dust(R, C, A)
        air_clean(up, down, R, C, A)

    return calc_dust(R, C, A)


R, C, T = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(R)]
print(solution(R, C, T, A))
