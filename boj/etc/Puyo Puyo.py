import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


def find_block(board):
    visit = [[False for _ in range(6)] for _ in range(12)]
    blocks = []

    for i in range(12):
        for j in range(6):
            if not visit[i][j] and board[i][j] != '.':
                item = board[i][j]
                block = [(i, j)]
                Q = collections.deque()
                Q.append((i, j))
                visit[i][j] = True

                while Q:
                    r, c = Q.popleft()

                    for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                        new_r = r + direct[0]
                        new_c = c + direct[1]

                        if 0 <= new_r < 12 and 0 <= new_c < 6 and not visit[new_r][new_c] and board[new_r][
                            new_c] == item:
                            Q.append((new_r, new_c))
                            visit[new_r][new_c] = True
                            block.append((new_r, new_c))

                if len(block) >= 4:
                    blocks.append(block)

    return blocks


def remove_block(board, blocks):
    for block in blocks:
        for r, c in block:
            board[r][c] = '.'


def down_item(board):
    for j in range(6):
        for i in range(11, 0, -1):
            if board[i][j] != '.':
                continue
            for find_i in range(i - 1, -1, -1):
                if board[find_i][j] != '.':
                    board[i][j] = board[find_i][j]
                    board[find_i][j] = '.'
                    break


def solution(board):
    answer = 0

    while True:
        blocks = find_block(board)
        if not blocks:
            break
        remove_block(board, blocks)
        down_item(board)
        answer += 1
    return answer


board = [list(input()) for _ in range(12)]
print(solution(board))
