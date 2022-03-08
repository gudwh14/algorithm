def print_board(board):
    for bo in board:
        print(bo)
    print()


def compare(x, y):
    x_i, x_j, x_count, x_empty = x
    y_i, y_j, y_count, y_empty = y

    if x_count > y_count:
        return 1
    elif x_count == y_count:
        if x_empty > y_empty:
            return 1
        elif x_empty == y_empty:
            if x_i > y_i:
                return -1
            elif x_i == y_i:
                if x_j > y_j:
                    return -1
            else:
                return 1
        else:
            return -1
    else:
        return -1


def set_sit(N, board, student, likes):
    find = []
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    max_count = -1
    max_empty = -1

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                count = 0
                empty = 0
                for direct in directions:
                    ni = i + direct[0]
                    nj = j + direct[1]

                    if 0 <= ni < N and 0 <= nj < N:
                        if board[ni][nj] in likes:
                            count += 1
                        elif board[ni][nj] == 0:
                            empty += 1

                if count > max_count:
                    find = [i, j]
                    max_count = count
                    max_empty = empty
                elif count == max_count:
                    if empty > max_empty:
                        find = [i, j]
                        max_count = count
                        max_empty = empty
                    elif empty == max_empty:
                        if i < find[0]:
                            find = [i, j]
                            max_count = count
                            max_empty = empty
                        elif i == find[0]:
                            if j < find[1]:
                                find = [i, j]
                                max_count = count
                                max_empty = empty

    board[find[0]][find[1]] = student


def solution(N, like):
    answer = 0
    board = [[0 for _ in range(N)] for _ in range(N)]

    for key, value in like.items():
        set_sit(N, board, key, value)

    for i in range(N):
        for j in range(N):
            count = 0
            student = board[i][j]

            for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                ni = i + direct[0]
                nj = j + direct[1]

                if 0 <= ni < N and 0 <= nj < N:
                    if board[ni][nj] in like[student]:
                        count += 1

            if count == 1:
                answer += 1
            elif count == 2:
                answer += 10
            elif count == 3:
                answer += 100
            elif count == 4:
                answer += 1000

    return answer


N = int(input())
like = {}
for _ in range(N * N):
    _input = list(map(int, input().split()))
    like[_input[0]] = _input[1:]

print(solution(N, like))
