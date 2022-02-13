from sys import stdin
import collections
import copy

# 위로 기울이는 함수
def up(n, m, board):
    red, blue = False, False
    count = 0

    for j in range(1, m - 1):
        for i in range(1, n - 1):
            if board[i][j] == 'R' or board[i][j] == 'B':
                index = i
                while index > 1:
                    # R, B 이동
                    if board[index][j] == 'R' or board[index][j] == 'B':
                        if board[index - 1][j] == '.':
                            board[index - 1][j] = board[index][j]
                            board[index][j] = '.'
                            count += 1
                        # 구멍을 만나면 해당 구슬을 없애고, True 로 설정
                        if board[index - 1][j] == 'O':
                            if board[index][j] == 'R':
                                red = True
                            elif board[index][j] == 'B':
                                blue = True
                            board[index][j] = '.'
                            count += 1
                    index -= 1

    return red, blue, count, board

# 아래로 기울이는 함수
def down(n, m, board):
    red, blue = False, False
    count = 0

    for j in range(1, m - 1):
        for i in range(n - 1, 0, -1):
            if board[i][j] == 'R' or board[i][j] == 'B':
                index = i
                while index < n - 1:
                    if board[index][j] == 'R' or board[index][j] == 'B':
                        if board[index + 1][j] == '.':
                            board[index + 1][j] = board[index][j]
                            board[index][j] = '.'
                            count += 1
                        if board[index + 1][j] == 'O':
                            if board[index][j] == 'R':
                                red = True
                            elif board[index][j] == 'B':
                                blue = True
                            board[index][j] = '.'
                            count += 1
                    index += 1
    return red, blue, count, board

# 오른쪽으로 기울이는 함수
def right(n, m, board):
    red, blue = False, False
    count = 0

    for i in range(1, n - 1):
        for j in range(m - 1, 0, -1):
            if board[i][j] == 'R' or board[i][j] == 'B':
                index = j
                while index < m - 1:
                    if board[i][index] == 'R' or board[i][index] == 'B':
                        if board[i][index + 1] == '.':
                            board[i][index + 1] = board[i][index]
                            board[i][index] = '.'
                            count += 1
                        if board[i][index + 1] == 'O':
                            if board[i][index] == 'R':
                                red = True
                            elif board[i][index] == 'B':
                                blue = True
                            board[i][index] = '.'
                            count += 1
                    index += 1
    return red, blue, count, board

# 왼쪽으로 기울이는 함수
def left(n, m, board):
    red, blue = False, False
    count = 0

    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if board[i][j] == 'R' or board[i][j] == 'B':
                index = j
                while index > 1:
                    if board[i][index] == 'R' or board[i][index] == 'B':
                        if board[i][index - 1] == '.':
                            board[i][index - 1] = board[i][index]
                            board[i][index] = '.'
                            count += 1
                        if board[i][index - 1] == 'O':
                            if board[i][index] == 'R':
                                red = True
                            elif board[i][index] == 'B':
                                blue = True
                            board[i][index] = '.'
                            count += 1
                    index -= 1
    return red, blue, count, board


def solution(n, m, board):
    answer = float('+inf')
    board = [list(b) for b in board]
    Q = collections.deque()
    Q.append([board, 1])

    while Q:
        board, times = Q.popleft()
        # 10번이 넘어가면 스킵
        if times > 10:
            continue
        u_r, u_b, u_c, u_board = up(n, m, copy.deepcopy(board))
        d_r, d_b, d_c, d_board = down(n, m, copy.deepcopy(board))
        l_r, l_b, l_c, l_board = left(n, m, copy.deepcopy(board))
        r_r, r_b, r_c, r_board = right(n, m, copy.deepcopy(board))

        # RED 가 구멍에 빠졋을경우 가장작은 회수로 초기화
        if (u_r and not u_b) or (d_r and not d_b) or (l_r and not l_b) or (r_r and not r_b):
            answer = min(answer, times)
            continue

        # 구슬이 움직일수있고, BLUE 가 구멍에 빠지지 않았을경우에, 보드 기울이기
        if u_c and not u_b:
            Q.append([u_board, times + 1])
        if d_c and not d_b:
            Q.append([d_board, times + 1])
        if l_c and not l_b:
            Q.append([l_board, times + 1])
        if r_c and not r_b:
            Q.append([r_board, times + 1])

    if answer == float('+inf'):
        answer = -1
    return answer


n, m = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(n)]

print(solution(n, m, board))

print(solution(5, 5, ['#####', '#..B#', '#.#.#', '#RO.#', '#####']))
print(solution(7, 7, ['#######', '#...RB#', '#.#####', '#.....#', '#####.#', '#O....#', '#######']))
print(solution(7, 7, ['#######', '#..R#B#', '#.#####', '#.....#', '#####.#', '#O....#', '#######']))
print(solution(10,10, [
'##########',
'#R#...##B#',
'#...#.##.#',
'#####.##.#',
'#......#.#',
'#.######.#',
'#.#....#.#',
'#.#.#.#..#',
'#...#.O#.#',
'##########']))
print(solution(3, 7,
['#######',
'#R.O.B#',
'#######']))
print(solution(10, 10, [
    '##########',
    '#R#...##B#',
    '#...#.##.#',
    '#####.##.#',
    '#......#.#',
    '#.######.#',
    '#.#....#.#',
    '#.#.##...#',
    '#O..#....#',
    '##########']))
print(solution(3, 10, ['##########', '#.O....RB#', '##########']))
