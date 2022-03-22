import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


def solution(n, m, board):
    coin_1 = None
    coin_2 = None

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'o':
                if not coin_1:
                    coin_1 = (i, j)
                else:
                    coin_2 = (i, j)

    Q = collections.deque()
    Q.append((coin_1, coin_2, 0))

    while Q:
        coin_1, coin_2, result = Q.popleft()

        if result >= 10:
            return -1

        for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            count = 0
            move = 0
            new_coin_1 = (coin_1[0] + direct[0], coin_1[1] + direct[1])
            new_coin_2 = (coin_2[0] + direct[0], coin_2[1] + direct[1])

            if 0 <= new_coin_1[0] < n and 0 <= new_coin_1[1] < m:
                if board[new_coin_1[0]][new_coin_1[1]] == '#':
                    new_coin_1 = coin_1
                else:
                    board[coin_1[0]][coin_1[1]] = '.'
                    board[new_coin_1[0]][new_coin_1[1]] = 'o'
                    move += 1
            else:
                count += 1

            if 0 <= new_coin_2[0] < n and 0 <= new_coin_2[1] < m:
                if board[new_coin_2[0]][new_coin_2[1]] == '#':
                    new_coin_2 = coin_2
                else:
                    board[coin_2[0]][coin_2[1]] = '.'
                    board[new_coin_2[0]][new_coin_2[1]] = 'o'
                    move += 1
            else:
                count += 1

            if count == 1:
                return result + 1
            elif count == 0 and move > 0:
                Q.append((new_coin_1, new_coin_2, result + 1))


n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
print(solution(n, m, board))
