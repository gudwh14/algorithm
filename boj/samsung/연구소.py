import copy
import itertools
import sys

def print_board(board):
    for bo in board:
        print(bo)
    print()


# 벽 개수 세주는 함수
def count_wall(n, m, board):
    count = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                count += 1

    return count


# 곱 함수
def product_n_m(n, m):
    n = [i for i in range(n)]
    m = [j for j in range(m)]
    product = itertools.product(n, m)

    return list(product)


# 바이러스 퍼트리는 함수
def spread_virus(n, m, board):
    visit = []
    count = 0

    def dfs(i, j):
        nonlocal count
        if 0 <= i < n and 0 <= j < m:
            if (i, j) not in visit:
                visit.append((i, j))
                if board[i][j] == 0:
                    board[i][j] = 2
                    count += 1
                elif board[i][j] == 1:
                    return
                elif board[i][j] == 2:
                    count += 1

                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                if (i, j) not in visit:
                    dfs(i, j)

    # board 총 개수에서 바이러스 카운팅빼준값을 리턴
    return n * m - count


def solution(n, m, board):
    answer = []
    # 벽의 개수 카운팅
    wall_count = count_wall(n, m, board) + 3
    # 벽을 세울 좌표들 만들기
    product = product_n_m(n, m)

    # 벽을 세울 좌표 3개를 뽑은 조합에대한 반복
    for comb in list(itertools.combinations(product, 3)):
        # board 복사
        _board = copy.deepcopy(board)
        flag = False
        # 해당 좌표들이 벽이거나 바이러스이면, 새로운 벽을 세울수 없다 -> 스킵
        for i, j in comb:
            if _board[i][j] == 1 or _board[i][j] == 2:
                flag = True
                break
            else:
                _board[i][j] = 1
        if flag:
            continue
        # 새로 세워진 벽을 기준으로, 바이러스 퍼트리기
        # 리턴된 값에서 벽의 개수를 뺀 값을 저장하기
        count = spread_virus(n, m, _board) - wall_count
        answer.append(count)

    # 오름차순으로 정렬
    answer.sort()
    # 마지막값 리턴
    return answer[-1]


# 0: 빈칸, 1: 벽, 2: 바이러스
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, m, board))
