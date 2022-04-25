import itertools
import sys


# 벽 개수 세주는 함수
def count_wall(n, m, board):
    count = 0
    wall_possible = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                count += 1
            if board[i][j] == 0:
                wall_possible.append((i, j))

    return count + 3, wall_possible


# 바이러스 퍼트리는 함수
def spread_virus(n, m, board):
    visit = [[False for _ in range(m)] for _ in range(n)]
    count = 0

    def dfs(i, j):
        nonlocal count
        if 0 <= i < n and 0 <= j < m:
            if not visit[i][j]:
                visit[i][j] = True
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
                if not visit[i][j]:
                    dfs(i, j)

    # board 총 개수에서 바이러스 카운팅빼준값을 리턴
    return n * m - count


def solution(n, m, board):
    answer = 0
    # 벽의 개수, 벽을 새로 세울수있는 좌표 구하기
    wall_count, wall_possible = count_wall(n, m, board)

    # 벽을 세울 좌표 3개를 뽑은 조합에대한 반복
    for comb in list(itertools.combinations(wall_possible, 3)):
        # board 복사
        _board = [item[:] for item in board]
        for i, j in comb:
            _board[i][j] = 1
        # 새로 세워진 벽을 기준으로, 바이러스 퍼트리기
        # 리턴된 값에서 벽의 개수를 뺀 값을 저장하기
        count = spread_virus(n, m, _board) - wall_count
        answer = max(answer, count)

    return answer


# 0: 빈칸, 1: 벽, 2: 바이러스
n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, m, board))
