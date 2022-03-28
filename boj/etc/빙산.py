import sys

sys.setrecursionlimit(10 ** 6)


def find_ices(N, M, board):
    ices = []

    for i in range(N):
        for j in range(M):
            if board[i][j] > 0:
                ices.append((i, j, board[i][j]))

    return ices


def district_ices(N, M, board, ices):
    visit = [[False for _ in range(M)] for _ in range(N)]
    count = 0

    def dfs(r, c):
        visit[r][c] = True
        for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = r + direct[0]
            new_c = c + direct[1]

            if 0 <= new_r < N and 0 <= new_c < M and not visit[new_r][new_c] and board[new_r][new_c] > 0:
                dfs(new_r, new_c)

    for r, c, height in ices:
        if not visit[r][c]:
            dfs(r, c)
            count += 1
    return count


def melt_ices(N, M, board, ices):
    for i in range(len(ices)):
        r, c, height = ices[i]

        count = 0
        for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            s_r = r + direct[0]
            s_c = c + direct[1]

            if 0 <= s_r < N and 0 <= s_c < M and board[s_r][s_c] <= 0:
                count += 1

        height -= count
        ices[i] = (r, c, height)

    ices.sort(key=lambda x: x[2], reverse=True)

    while ices and ices[-1][2] <= 0:
        r, c, height = ices[-1]
        board[r][c] = 0
        ices.pop()


def solution(N, M, board):
    answer = 0
    ices = find_ices(N, M, board)

    while True:
        district = district_ices(N, M, board, ices)
        if district >= 2:
            break
        if district == 0 or not ices:
            return 0
        melt_ices(N, M, board, ices)
        answer += 1

    return answer


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
