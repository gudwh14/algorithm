import math


def print_board(board):
    for bo in board:
        print(bo)
    print()


def init_board(board, fire_info, M):
    for idx in range(M):
        r, c, m, s, d = fire_info[idx]
        fire_info[idx] = [r - 1, c - 1, m, s, d]
        board[r - 1][c - 1].append(idx)


# 파이어볼 움직이기
def move_fire(board, fire_info, N, remove_fire):
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    for idx in range(len(fire_info)):
        # 제거된 파이어볼 이면 이동 X
        if remove_fire[idx]:
            continue
        r, c, m, s, d = fire_info[idx]

        new_r = r + directions[d][0] * s
        new_c = c + directions[d][1] * s

        if new_r < 0:
            new_r = N - abs(new_r) % N
        if new_r >= N:
            new_r = new_r % N

        if new_c < 0:
            new_c = N - abs(new_c) % N
        if new_c >= N:
            new_c = new_c % N

        # 원래자리에서 삭제
        board[r][c].remove(idx)
        # 새로운자리로 이동
        board[new_r][new_c].append(idx)
        # 파이어볼 정보 교체
        fire_info[idx] = [new_r, new_c, m, s, d]


def split_fire(board, fire_info, N, remove_fire):
    for i in range(N):
        for j in range(N):
            # 같은 칸에 2개 이상이면
            if len(board[i][j]) > 1:
                sum_m = 0
                sum_s = 0
                is_odd = None
                direct = False
                count = 0

                for idx in board[i][j]:
                    # 파이어볼 삭제
                    remove_fire[idx] = True
                    count += 1
                    r, c, m, s, d = fire_info[idx]
                    sum_m += m
                    sum_s += s
                    if is_odd == None:
                        if d % 2 == 0:
                            is_odd = False
                        else:
                            is_odd = True
                        direct = True
                    elif direct:
                        if is_odd:
                            if d % 2 == 0:
                                direct = False
                        else:
                            if d % 2 != 0:
                                direct = False

                new_s = math.floor(sum_s / count)
                new_m = math.floor(sum_m / 5)
                len_fire = len(fire_info)
                # 해당칸 파이어볼 삭제
                board[i][j].clear()
                if new_m > 0:
                    # 새로운 파이어볼 생성
                    for idx in range(4):
                        if direct:
                            new_d = idx * 2
                        else:
                            new_d = idx * 2 + 1
                        fire_info.append([i, j, new_m, new_s, new_d])
                        board[i][j].append(len_fire + idx)


def solution(N, M, K, fire_info):
    answer = 0
    board = [[[] for _ in range(N)] for _ in range(N)]
    remove_fire = [False for _ in range(1000000)]
    init_board(board, fire_info, M)

    for _ in range(K):
        move_fire(board, fire_info, N, remove_fire)
        split_fire(board, fire_info, N, remove_fire)

    for idx in range(len(fire_info)):
        if remove_fire[idx]:
            continue
        answer += fire_info[idx][2]

    return answer


N, M, K = map(int, input().split())
fire_info = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, K, fire_info))
