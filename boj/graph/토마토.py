def solution(N, M, board):
    tomatoes = []
    answer = 0
    total = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                tomatoes.append((i, j))
            elif board[i][j] == 0:
                total += 1

    while True:
        if total == 0:
            break

        if not tomatoes and total:
            return -1

        new_tomatoes = []
        count = 0
        for i, j in tomatoes:
            for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_i = i + direct[0]
                new_j = j + direct[1]

                if 0 <= new_i < N and 0 <= new_j < M and board[new_i][new_j] == 0:
                    new_tomatoes.append((new_i, new_j))
                    board[new_i][new_j] = 1
                    count += 1
        total -= count
        tomatoes = new_tomatoes
        answer += 1

    return answer


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
