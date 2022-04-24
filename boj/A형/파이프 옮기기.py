# BFS로 하면 시간초과
# DFS로 풀이시 방문처리 없이 통과가능

def solution(board):
    answer = 0
    # 0: 가로, 1: 세로, 2: 대각선

    if board[N - 1][N - 1] == 1:
        return answer

    def dfs(r, c, direction):
        if r == N - 1 and c == N - 1:
            nonlocal answer
            answer += 1
            return

        # 가로 이동
        if direction == 0 or direction == 2:
            if c < N - 1 and board[r][c + 1] == 0:
                dfs(r, c + 1, 0)

        # 세로이동
        if direction == 1 or direction == 2:
            if r < N - 1 and board[r + 1][c] == 0:
                dfs(r + 1, c, 1)

        # 대각선 이동
        if r < N - 1 and c < N - 1 and board[r + 1][c] == 0 and board[r][c + 1] == 0 and board[r + 1][c + 1] == 0:
            dfs(r + 1, c + 1, 2)

    dfs(0, 1, 0)

    return answer


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(board))
