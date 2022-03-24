import sys

sys.setrecursionlimit(10 ** 6)


def print_board(board):
    for bo in board:
        print(bo)
    print()


def find_in_air(N, M, board):
    visit = [[False for _ in range(M)] for _ in range(N)]
    result = []

    def dfs(i, j, airs):
        visit[i][j] = True
        airs.append((i, j))

        for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_i = i + direct[0]
            new_j = j + direct[1]

            if 0 <= new_i < N and 0 <= new_j < M and board[new_i][new_j] == 0 and not visit[new_i][new_j]:
                dfs(new_i, new_j, airs)

    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j] == 0:
                airs = []
                dfs(i, j, airs)
                result.append(airs)

    if len(result) > 1:
        for idx in range(1, len(result)):
            for r, c in result[idx]:
                board[r][c] = 2
        return sum(result[1:], [])
    else:
        return []


def solution(N, M, board):
    answer = 0
    cheeses = []

    in_airs = find_in_air(N, M, board)

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                cheeses.append((i, j))

    if not cheeses:
        return answer

    while True:
        answer += 1

        new_cheeses = []
        remove_cheeses = []
        for cheese in cheeses:
            i = cheese[0]
            j = cheese[1]
            count = 0
            for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                t_i = i + direct[0]
                t_j = j + direct[1]

                if 0 <= t_i < N and 0 <= t_j < M and board[t_i][t_j] == 0:
                    count += 1

            if count < 2:
                new_cheeses.append((i, j))
            elif count >= 2:
                remove_cheeses.append((i, j))

        if not new_cheeses:
            break
        for r, c in remove_cheeses:
            board[r][c] = 0
        for r, c in in_airs:
            board[r][c] = 0
        in_airs = find_in_air(N, M, board)
        cheeses = new_cheeses[:]

    return answer


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
