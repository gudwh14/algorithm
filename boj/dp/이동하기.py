def solution(N, M, board):
    dp = [[0 for _ in range(M)] for _ in range(N)]
    dp[0][0] = board[0][0]
    for r in range(N):
        for c in range(M):
            if 0 <= r - 1 < N and 0 <= c - 1 < M:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1]) + board[r][c]
            elif r - 1 < 0:
                dp[r][c] = dp[r][c - 1] + board[r][c]
            elif c - 1 < 0:
                dp[r][c] = dp[r - 1][c] + board[r][c]

    return dp[N - 1][M - 1]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
