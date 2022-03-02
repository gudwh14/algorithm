def print_board(board):
    for bo in board:
        print(bo)
    print()


def init(N, K, board, smell, d_shark):
    shark_info = {}
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                shark_info[board[i][j]] = (i, j, d_shark[board[i][j]])
                smell[i][j] = (board[i][j], K)
    return shark_info


def move(N, K, shark_board, shark, shark_info, smell, pr_shark, answer):
    # 상, 하, 좌, 우
    directions = [(), (-1, 0), (1, 0), (0, -1), (0, 1)]
    move_info = []

    for idx in shark:
        # 상어의 좌표와 방향 가져오기
        i, j, d = shark_info[idx]
        # 상어가 이동 가능한 좌표들 저장
        find = []
        # 이동할 좌표
        move = ()

        # 냄새가 없는 칸의 이동 가능한 좌표 찾기
        for d_idx in range(1, 5):
            new_i = i + directions[d_idx][0]
            new_j = j + directions[d_idx][1]

            if 0 <= new_i < N and 0 <= new_j < N and (not smell[new_i][new_j] or smell[new_i][new_j][1] - answer < 0):
                find.append((idx, new_i, new_j, d_idx))
        # 냄새가 없는 칸으로 이동 할 수 있으면
        if find:
            # 이동 가능한 칸이 1칸 보다 많을때 우선순위 찾기
            if len(find) > 1:
                priority = pr_shark[idx - 1][d - 1]
                for direct in priority:
                    for data in find:
                        idx, mi, mj, md = data
                        if direct == md:
                            move = data
                            break
                    if move:
                        break
            else:
                move = find[0]

        # 냄새가 없는 칸이 없을경우
        # 자신의 냄새가 있는칸을 방향으로 잡는다.
        else:
            for d_idx in range(1, 5):
                new_i = i + directions[d_idx][0]
                new_j = j + directions[d_idx][1]

                if 0 <= new_i < N and 0 <= new_j < N and smell[new_i][new_j][0] == idx and smell[new_i][
                    new_j][1] - answer >= 0:
                    find.append((idx, new_i, new_j, d_idx))

            if len(find) > 1:
                priority = pr_shark[idx - 1][d - 1]
                for direct in priority:
                    for data in find:
                        idx, mi, mj, md = data
                        if direct == md:
                            move = data
                            break
                    if move:
                        break
            else:
                move = find[0]

        if move:
            shark_board[i][j].clear()
            move_info.append(move)
    # print(move_info)
    # 상어 이동
    for moves in move_info:
        idx, i, j, d = moves
        shark_info[idx] = (i, j, d)
        shark_board[i][j].append(idx)

    # print_board(shark_board)
    # 같은 칸 상어 잡아 먹기
    # 항상 상어들은 오름차순으로 정렬되어있음
    for i in range(N):
        for j in range(N):
            if len(shark_board[i][j]) > 1:
                for num in shark_board[i][j][1:]:
                    shark.remove(num)
    # 냄새 풍기기
    for idx in shark:
        i, j, d = shark_info[idx]
        smell[i][j] = (idx, answer + K)
    # print_board(smell)


def solution(N, M, K, board, pr_shark, d_shark):
    answer = 1
    # 냄새 정보를 가지고있는 배열
    smell = [[[] for _ in range(N)] for _ in range(N)]
    shark_board = [[[] for _ in range(N)] for _ in range(N)]
    # 상어 위치, 방향 정보
    shark_info = init(N, K, board, smell, d_shark)
    # 남아 있는 상어
    shark = [num for num in range(1, M + 1)]

    while True:
        # 1000초가 지나면 실패
        if answer > 1000:
            return -1
        # 상어 움직이기
        move(N, K, shark_board, shark, shark_info, smell, pr_shark, answer)
        # 남은상어가 1마리 이면 성공
        if len(shark) == 1:
            break
        answer += 1
    return answer


N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
d_shark = list(map(int, input().split()))
d_shark.insert(0, 0)
pr_shark = []
for _ in range(M):
    pr_shark.append([list(map(int, input().split())) for _ in range(4)])

print(solution(N, M, K, board, pr_shark, d_shark))
