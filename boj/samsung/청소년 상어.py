import collections
import copy


def move_fish(shark_info, fish_info, fish_num, board):
    directions = [(), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
    # 해당 물고기의 현재 위치 가져오기
    i, j = fish_info[fish_num]
    # 물고기의 방향 가져오기
    num, direct = board[i][j]
    # 상어 위치 정보
    si, sj, sd = shark_info
    for _ in range(7):
        new_i = i + directions[direct][0]
        new_j = j + directions[direct][1]

        # 물고기가 이동할 칸이 상어가 있는 칸이거나, 배열을 벗어나면 이동 불가
        if (new_i, new_j) != (si, sj) and 0 <= new_i < 4 and 0 <= new_j < 4:
            # 물고기가 있으면 서로 교체
            if board[new_i][new_j]:
                t_num = board[new_i][new_j][0]
                temp = board[new_i][new_j]
                board[new_i][new_j] = [num, direct]
                board[i][j] = temp
                fish_info[fish_num] = (new_i, new_j)
                fish_info[t_num] = (i, j)
            # 없으면 그냥 이동
            else:
                board[new_i][new_j] = [num, direct]
                board[i][j].clear()
                fish_info[fish_num] = (new_i, new_j)
            break
        # 45도씩 회전
        else:
            direct += 1
            if direct == 9:
                direct = 1


# 상어 이동
def move_shark(shark_info, shark_move, catch_fish, new_board):
    # 상어가 이동할 좌표
    i, j = shark_move
    # 잡은 물고기에 추가
    catch_fish.append(new_board[i][j][0])
    # 상어 좌표 새롭게 설정, 이동한 좌표, 해당 물고기의 방향
    shark_info = [i, j, new_board[i][j][1]]
    new_board[i][j].clear()

    return shark_info


def solution(board):
    answer = 0
    # 물고기 좌표를 저장하는 hash
    # fish_info[물고기 번호] = [x좌표, y좌표]
    fish_info = {}
    # 상어가 잡아먹은 물고기 번호를 저장하는 변수
    catch_fish = []

    # 물고기 좌표 저장
    for i in range(4):
        for j in range(len(board[0])):
            num, direct = board[i][j]
            fish_info[num] = (i, j)

    # 맨처음 상어가 (0,0) 물고기 잡아먹기
    shark_info = [0, 0, board[0][0][1]]
    catch_fish.append(board[0][0][0])
    board[0][0].clear()

    # BFS 탐색
    Q = collections.deque()
    Q.append((shark_info, catch_fish, fish_info, board))
    while Q:
        shark_info, catch_fish, fish_info, board = Q.popleft()
        # 상어가 움직일수 있는 방향
        directions = [(), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

        # 물고기 좌표 정보 복사
        _fish_info = copy.deepcopy(fish_info)
        # 물고기 이동하기
        for idx in range(1, 17):
            # 잡아 먹히지 않은 물고기만 이동
            if idx not in catch_fish:
                move_fish(shark_info, _fish_info, idx, board)

        # 상어가 이동할수 있는 좌표
        shark_moves = []
        for idx in range(1, 4):
            si, sj, sd = shark_info
            new_si = si + directions[sd][0] * idx
            new_sj = sj + directions[sd][1] * idx
            # 칸을 벗어나거나, 해당칸에 물고기가 없으면 이동할수 없음
            if 0 <= new_si < 4 and 0 <= new_sj < 4 and board[new_si][new_sj]:
                shark_moves.append((new_si, new_sj))
        # 상어가 이동할수 있는 칸이 없으면 종료
        if not shark_moves:
            # 잡아먹은 물고기의 총합 구하기
            answer = max(answer, sum(catch_fish))
            continue

        # 상어 이동
        for shark_move in shark_moves:
            _catch_fish = catch_fish[:]
            # 3차원 배열 4 * 4 copy를 이용해 복사
            _board = copy.deepcopy(board)
            _shark_info = move_shark(shark_info, shark_move, _catch_fish, _board)
            Q.append((_shark_info, _catch_fish, _fish_info, _board))
    return answer


board = [[[] for _ in range(4)] for _ in range(4)]
fish = [list(map(int, input().split())) for _ in range(4)]

# board 배열에 물고기 정보 저장하기
# board[i][j] = [물고기 번호, 물고기 방향]
for i in range(4):
    info = []
    for j in range(len(fish[0])):
        info.append(fish[i][j])
        if len(info) == 2:
            board[i][(j + 1) // 2 - 1] = info
            info = []

print(solution(board))
