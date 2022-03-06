def print_board(board):
    for bo in board:
        print(bo)
    print()


# 각 방향으로 모래 흩날리는 함수 만들기
def spread_dust_left(r, c):
    result = 0

    dust = A[r][c]
    seven = int(dust * 0.07)
    one = int(dust * 0.01)
    ten = int(dust * 0.1)
    two = int(dust * 0.02)
    five = int(dust * 0.05)
    alpha = dust - 2 * seven - 2 * one - 2 * ten - 2 * two - five

    directions = [(1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1), (2, 0), (-2, 0), (0, -1), (0, -2)]

    A[r][c] = 0

    for idx in range(len(directions)):
        if idx == 0 or idx == 1:
            add_dust = seven
        elif idx == 2 or idx == 3:
            add_dust = one
        elif idx == 4 or idx == 5:
            add_dust = ten
        elif idx == 6 or idx == 7:
            add_dust = two
        elif idx == 8:
            add_dust = alpha
        elif idx == 9:
            add_dust = five

        new_r = r + directions[idx][0]
        new_c = c + directions[idx][1]

        if 0 <= new_r < N and 0 <= new_c < N:
            A[new_r][new_c] += add_dust
        else:
            result += add_dust

    return result


def spread_dust_down(r, c):
    result = 0

    dust = A[r][c]
    seven = int(dust * 0.07)
    one = int(dust * 0.01)
    ten = int(dust * 0.1)
    two = int(dust * 0.02)
    five = int(dust * 0.05)
    alpha = dust - 2 * seven - 2 * one - 2 * ten - 2 * two - five

    directions = [(0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 2), (0, -2), (1, 0), (2, 0)]

    A[r][c] = 0

    for idx in range(len(directions)):
        if idx == 0 or idx == 1:
            add_dust = seven
        elif idx == 2 or idx == 3:
            add_dust = one
        elif idx == 4 or idx == 5:
            add_dust = ten
        elif idx == 6 or idx == 7:
            add_dust = two
        elif idx == 8:
            add_dust = alpha
        elif idx == 9:
            add_dust = five

        new_r = r + directions[idx][0]
        new_c = c + directions[idx][1]

        if 0 <= new_r < N and 0 <= new_c < N:
            A[new_r][new_c] += add_dust
        else:
            result += add_dust

    return result


def spread_dust_right(r, c):
    result = 0

    dust = A[r][c]
    seven = int(dust * 0.07)
    one = int(dust * 0.01)
    ten = int(dust * 0.1)
    two = int(dust * 0.02)
    five = int(dust * 0.05)
    alpha = dust - 2 * seven - 2 * one - 2 * ten - 2 * two - five

    directions = [(1, 0), (-1, 0), (1, -1), (-1, -1), (1, 1), (-1, 1), (2, 0), (-2, 0), (0, 1), (0, 2)]

    A[r][c] = 0

    for idx in range(len(directions)):
        if idx == 0 or idx == 1:
            add_dust = seven
        elif idx == 2 or idx == 3:
            add_dust = one
        elif idx == 4 or idx == 5:
            add_dust = ten
        elif idx == 6 or idx == 7:
            add_dust = two
        elif idx == 8:
            add_dust = alpha
        elif idx == 9:
            add_dust = five

        new_r = r + directions[idx][0]
        new_c = c + directions[idx][1]

        if 0 <= new_r < N and 0 <= new_c < N:
            A[new_r][new_c] += add_dust
        else:
            result += add_dust

    return result


def spread_dust_up(r, c):
    result = 0

    dust = A[r][c]
    seven = int(dust * 0.07)
    one = int(dust * 0.01)
    ten = int(dust * 0.1)
    two = int(dust * 0.02)
    five = int(dust * 0.05)
    alpha = dust - 2 * seven - 2 * one - 2 * ten - 2 * two - five

    directions = [(0, 1), (0, -1), (1, -1), (1, 1), (-1, -1), (-1, 1), (0, 2), (0, -2), (-1, 0), (-2, 0)]

    A[r][c] = 0

    for idx in range(len(directions)):
        if idx == 0 or idx == 1:
            add_dust = seven
        elif idx == 2 or idx == 3:
            add_dust = one
        elif idx == 4 or idx == 5:
            add_dust = ten
        elif idx == 6 or idx == 7:
            add_dust = two
        elif idx == 8:
            add_dust = alpha
        elif idx == 9:
            add_dust = five

        new_r = r + directions[idx][0]
        new_c = c + directions[idx][1]

        if 0 <= new_r < N and 0 <= new_c < N:
            A[new_r][new_c] += add_dust
        else:
            result += add_dust

    return result


def solution(N, A):
    answer = 0
    move = 0
    r, c = N // 2, N // 2

    # 토네이도 이동
    while True:
        # 토네이도가 움직이는 길이가 격자판 크기의 - 1이면 종료
        if move == N - 1:
            break
        move += 1
        for idx in range(1, move + 1):
            # print('left', r, c - idx)
            answer += spread_dust_left(r, c - idx)
        c -= move

        for idx in range(1, move + 1):
            # print('down', r + idx, c)
            answer += spread_dust_down(r + idx, c)
        r += move

        move += 1
        for idx in range(1, move + 1):
            # print('right', r, c + idx)
            answer += spread_dust_right(r, c + idx)
        c += move

        for idx in range(1, move + 1):
            # print('up', r - idx, c)
            answer += spread_dust_up(r - idx, c)
        r -= move

    # 마지막 토네이도는 왼쪽으로 격자판 크기만큼 움직임
    for idx in range(1, move + 1):
        answer += spread_dust_left(r, c - idx)
    c -= move

    return answer


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, A))
