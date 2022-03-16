import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


def solution(N, M, board):
    INF = float('+inf')
    answer = INF
    Q = collections.deque()

    visit = [[[False for _ in range(M)] for _ in range(N)] for _ in range(2)]
    visit[0][0][0] = True
    Q.append((0, 0, 0, 1))

    while Q:
        i, j, count, distance = Q.popleft()

        if i == N - 1 and j == M - 1:
            answer = min(answer, distance)
            continue

        for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_i = i + direct[0]
            new_j = j + direct[1]

            if 0 <= new_i < N and 0 <= new_j < M:
                if count == 1 and not visit[1][new_i][new_j]:
                    if board[new_i][new_j] == 0:
                        Q.append((new_i, new_j, count, distance + 1))
                        visit[1][new_i][new_j] = True
                elif count == 0:
                    if board[new_i][new_j] == 0 and not visit[0][new_i][new_j]:
                        Q.append((new_i, new_j, count, distance + 1))
                        visit[0][new_i][new_j] = True

                    elif board[new_i][new_j] == 1 and not visit[1][new_i][new_j]:
                        Q.append((new_i, new_j, count + 1, distance + 1))
                        visit[1][new_i][new_j] = True

    if answer == INF:
        return -1
    return answer


N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
print(solution(N, M, board))
