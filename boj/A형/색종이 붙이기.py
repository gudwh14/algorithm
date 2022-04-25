import collections


# 해당칸에 어떤 색종이를 붙일수 있는지 판단 하는 함수!
# 여러 종류의 색종이를 붙일수도 있다
def compare(i, j, board, counts):
    max_shape = []
    if board[i][j] == 1:
        if counts[0] > 0:
            max_shape.append(0)
        if i < 10 - 1 and j < 10 - 1 and board[i + 1][j + 1] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1:
            if counts[1] > 0:
                max_shape.append(1)
            if i < 10 - 2 and j < 10 - 2 and board[i + 2][j + 2] == 1 and board[i + 2][j] == 1 and board[i][
                j + 2] == 1 and board[i + 2][
                j + 1] == 1 and board[i + 1][j + 2] == 1:
                if counts[2] > 0:
                    max_shape.append(2)
                if i < 10 - 3 and j < 10 - 3 and board[i + 3][j + 3] == 1 and board[i + 3][j] == 1 and board[i][
                    j + 3] == 1 and board[i + 3][
                    j + 1] == 1 and board[i + 3][j + 2] == 1 and board[i + 1][j + 3] == 1 and board[i + 2][
                    j + 3] == 1:
                    if counts[3] > 0:
                        max_shape.append(3)
                    if i < 10 - 4 and j < 10 - 4 and board[i + 4][j + 4] == 1 and board[i + 4][j] == 1 and board[i][
                        j + 4] == 1 and board[i + 4][j + 1] == 1 and board[i + 4][j + 2] == 1 and board[i + 4][
                        j + 3] == 1 and board[i + 1][
                        j + 4] == 1 and board[i + 2][j + 4] == 1 and board[i + 3][j + 4] == 1:
                        if counts[4] > 0:
                            max_shape.append(4)
    return max_shape


# 색종이 붙이기
def update(i, j, board, shape, counts):
    for r in range(i, i + 1 + shape):
        for c in range(j, j + 1 + shape):
            board[r][c] = 2
    counts[shape] -= 1

    return counts


def solution(board):
    answer = float('+inf')
    counts = [5, 5, 5, 5, 5]
    total = 0

    # 색종이를 붙여야하는 칸의 개수 구하기
    for i in range(10):
        for j in range(10):
            if board[i][j] == 1:
                total += 1

    Q = collections.deque()
    Q.append((board, total, counts))

    while Q:
        board, total, counts = Q.popleft()

        # 색종이를 모든칸에 다 붙였을경우 사용한 색종이 개수 구하기
        if total == 0:
            answer = min(answer, 25 - sum(counts))
            continue

        flag = False
        for i in range(10):
            for j in range(10):
                # 색종이를 붙여야하는 칸이면 로직 실행
                if board[i][j] == 1:
                    # 붙일수있는 색종이 종류 구하기
                    shape_list = compare(i, j, board, counts)
                    # 각 색종이를 붙일수 있는 경우의 수를 큐에 저장
                    for item in shape_list:
                        _board = [i[:] for i in board]
                        _counts = counts[:]
                        update(i, j, _board, item, _counts)
                        Q.append((_board, total - pow(item + 1, 2), _counts))
                    # 반복문 종료!
                    flag = True
                if flag:
                    break
            if flag:
                break

    # 만약 색종이를 붙일 수 없으면 -1 리턴
    if answer == float('+inf'):
        return -1
    return answer


board = [list(map(int, input().split())) for _ in range(10)]
print(solution(board))
