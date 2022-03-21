def solution(N, board):
    dp = [[-1 for _ in range(N)] for _ in range(N)]

    def dfs(i, j):
        # 도착지에 만나면 1반환
        if i == N - 1 and j == N - 1:
            return 1
        # 좌표 예외 처리
        if not (0 <= i < N and 0 <= j < N):
            return 0
        # 더이상 이동 할 수 없는 좌표
        if board[i][j] == 0:
            return 0

        # (i, j)를 아직 방문하지 않았으면 다음 방문 탐색
        if dp[i][j] == -1:
            # 방문 처리
            dp[i][j] = 0

            # dp 더하기
            dp[i][j] += dfs(i + 1 * board[i][j], j) + dfs(i, j + 1 * board[i][j])
        return dp[i][j]

    return dfs(0, 0)


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))
