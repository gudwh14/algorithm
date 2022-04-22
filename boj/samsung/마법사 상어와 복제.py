import collections
import copy


# 물고기 복사하기
def copy_fish(board):
    _board = copy.deepcopy(board)
    return _board


# 물고기 이동
def move_fish(board, shark, smells):
    # 이동 방향
    directions = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    # 새로운 물고기 board
    new_board = collections.defaultdict(list)
    for i in range(1, 5):
        for j in range(1, 5):
            # 물고기가 존재하는 칸만 이동
            if board[(i, j)]:
                # 물고기 방향 d 가져오기
                for d in board[(i, j)]:
                    # 방향 45씩 반시계로 회전
                    for idx in range(8):
                        _d = d - idx
                        if _d <= 0:
                            _d += 8
                        new_i = i + directions[_d][0]
                        new_j = j + directions[_d][1]

                        # 격자를 벗어나지않고 냄새도 없고 상어도 없는 칸이면 이동 가능!
                        if 1 <= new_i <= 4 and 1 <= new_j <= 4 and [new_i, new_j] != shark and smells[new_i][
                            new_j] == 0:
                            new_board[(new_i, new_j)].append(_d)
                            break
                    # 이동 불가할 경우 제자리
                    else:
                        new_board[(i, j)].append(d)
    return new_board


# 상어 이동
def move_shark(board, shark, smells):
    # 상어 이동방향
    directions = [(), (-1, 0), (0, -1), (1, 0), (0, 1)]
    Q = collections.deque()
    # 상어 좌표
    i, j = shark[0], shark[1]
    # 상어가 이동한 칸의 정보
    Q.append((i, j, '', 0, []))

    while Q and len(Q[0][2]) < 3:
        # 좌표, 방향, 물고기 개수, 먹은 물고기 정보
        r, c, d, fish, eat = Q.popleft()

        # 상어 4방향 이동
        for idx in range(1, 5):
            new_r = r + directions[idx][0]
            new_c = c + directions[idx][1]

            # 격자를 벗어나지 않으면 이동
            if 1 <= new_r <= 4 and 1 <= new_c <= 4:
                _eat = eat[:]
                _fish = fish
                # 이미 먹은 물고기가 아니면 먹기
                if (new_r, new_c) not in _eat:
                    _eat.append((new_r, new_c))
                    # 해당칸의 모든 물고기 다 먹기
                    _fish += len(board[(new_r, new_c)])
                _d = d
                # 방향 더하기
                _d += str(idx)
                Q.append((new_r, new_c, _d, _fish, _eat))
    Q = list(Q)
    # 물고기 먹은순, 이동방향 사전순으로 정렬
    Q.sort(key=lambda x: (x[3], -int(x[2])))

    # 먹은 물고기가 존재하면 물고기 제거 및 냄새 남기기
    if Q[-1][3] > 0:
        moves = Q[-1][2]
        for move in moves:
            i = i + directions[int(move)][0]
            j = j + directions[int(move)][1]
            if board[(i, j)]:
                smells[i][j] = 3
            board[(i, j)].clear()

    # 이동한 상어 좌표 반환
    return [Q[-1][0], Q[-1][1]]


def solution(fishes, shark):
    smells = [[0 for _ in range(5)] for _ in range(5)]
    board = collections.defaultdict(list)
    answer = 0

    for fish in fishes:
        x, y, d = fish
        board[(x, y)].append(d)

    for _ in range(S):
        _board = copy_fish(board)
        board = move_fish(board, shark, smells)
        shark = move_shark(board, shark, smells)

        # 물고기 복제 및 냄새 -1
        for i in range(1, 5):
            for j in range(1, 5):
                if _board[(i, j)]:
                    board[(i, j)].extend(_board[(i, j)])
                if smells[i][j] > 0:
                    smells[i][j] -= 1

    # 격자에 남아있는 물고기 총 수 구하기
    for i in range(1, 5):
        for j in range(1, 5):
            answer += len(board[(i, j)])
    return answer


M, S = map(int, input().split())
fishes = [list(map(int, input().split())) for _ in range(M)]
shark = list(map(int, input().split()))
print(solution(fishes, shark))
