import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


def solution(n, m, r, c, d, board):
    answer = 0
    # 왼쪽 방향으로 좌표 이동 값 // 북, 동, 남, 서
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    # 후진 좌표이동 방향 저장 배열
    back_directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    Q = collections.deque()
    # 초기 큐: (현재 좌표, 현재 방향)
    Q.append((r, c, d))

    while Q:
        ni, nj, d = Q.popleft()
        # 청소할수있으면 청소
        if board[ni][nj] == 0:
            answer += 1
            board[ni][nj] = 2

        # 4 방향 모두 확인
        find = False
        for i in range(4):
            # 현재 방향에서 왼쪽 방향으로 탐색
            move_i, move_j = directions[d]
            # 청소 할수있으면 해당 방향으로 이동
            if board[ni + move_i][nj + move_j] == 0:
                d -= 1
                if d == -1:
                    d = 3
                Q.append((ni + move_i, nj + move_j, d))
                # 종료
                find = True
                break
            # 청소 할수 없으면 현재 방향 -> 왼쪽 방향으로 전환
            d -= 1
            if d == -1:
                d = 3

        # 청소 할수있는 칸을 찾으면 스킵
        if find:
            continue
        # 청소 할수있는 칸이 없고
        # 후진 할수 없으면 종료!
        if board[ni + back_directions[d][0]][nj + back_directions[d][1]] == 1:
            break
        # 후진
        else:
            Q.append((ni + back_directions[d][0], nj + back_directions[d][1], d))

    return answer


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, m, r, c, d, board))
