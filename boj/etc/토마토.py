def print_board(board):
    for bo in board:
        print(bo)
    print()


def solution(M, N, H, board):
    answer = 0
    total_tomato = 0
    done_tomatoes = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (N, 0), (-N, 0)]

    for i in range(N * H):
        for j in range(M):
            if board[i][j] != -1:
                total_tomato += 1
            if board[i][j] == 1:
                done_tomatoes.append((i, j))

    now_tomato = len(done_tomatoes)

    while True:
        if total_tomato == now_tomato:
            break
        if not done_tomatoes:
            return -1

        answer += 1
        new_done_tomatoes = []
        for r, c in done_tomatoes:
            for direct in range(len(directions)):
                new_r = r + directions[direct][0]
                new_c = c + directions[direct][1]

                if direct == 0 or direct == 2:
                    # 격자를 넘어가면 X
                    if r // N + 1 == new_r // N or r // N - 1 == new_r // N:
                        continue
                if 0 <= new_r < N * H and 0 <= new_c < M and board[new_r][new_c] == 0:
                    board[new_r][new_c] = 1
                    new_done_tomatoes.append((new_r, new_c))

        now_tomato += len(new_done_tomatoes)
        done_tomatoes = new_done_tomatoes[:]

    return answer


M, N, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N * H)]
print(solution(M, N, H, board))
