import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


def rotate90(l, N, A):
    n = pow(2, N)
    l = pow(2, l)
    new_A = [[0 for _ in range(n)] for _ in range(n)]

    # 90도 회전
    for i in range(0, n, l):
        idx = 1
        for j in range(0, n, l):
            c_idx = 0
            for r in range(i, i + l):
                r_idx = i
                for c in range(j, j + l):
                    new_A[r_idx][l * idx - c_idx - 1] = A[r][c]
                    r_idx += 1
                c_idx += 1
            idx += 1

    total = 0
    direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    find = []
    # 녹는 얼음 찾기
    for i in range(n):
        for j in range(n):
            if new_A[i][j] > 0:
                if i == 0 and (j == 0 or j == n - 1) or i == n - 1 and (j == 0 or j == n - 1):
                    # new_A[i][j] -= 1
                    find.append((i, j))
                else:
                    count = 0
                    for direct in direction:
                        ni = i + direct[0]
                        nj = j + direct[1]
                        if 0 <= ni < n and 0 <= nj < n and new_A[ni][nj] > 0:
                            count += 1
                    if count < 3:
                        # new_A[i][j] -= 1
                        find.append((i, j))

                if new_A[i][j] > 0:
                    total += new_A[i][j]

    # 얼음 녹이기
    for i, j in find:
        new_A[i][j] -= 1
        total -= 1

    return new_A, total


# 가장 큰 얼음 덩어리 찾기
def find_big_ice(A, N):
    result = 0
    n = pow(2, N)
    visit = [[False for _ in range(n)] for _ in range(n)]

    def bfs(i, j):
        res = 1
        Q = collections.deque()
        direction = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        Q.append((i, j, 1))
        visit[i][j] = True

        while Q:
            ni, nj, count = Q.popleft()

            for direct in direction:
                new_i = ni + direct[0]
                new_j = nj + direct[1]
                if 0 <= new_i < n and 0 <= new_j < n and A[new_i][new_j] > 0 and not visit[new_i][new_j]:
                    Q.append((new_i, new_j, count + 1))
                    res += 1
                    visit[new_i][new_j] = True
        return res

    for i in range(n):
        for j in range(n):
            if A[i][j] > 0:
                result = max(result, bfs(i, j))

    return result


def solution(N, A, L):
    total = 0
    for l in L:
        A, total = rotate90(l, N, A)

    print(total)
    print(find_big_ice(A, N))


N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(pow(2, N))]
L = list(map(int, input().split()))
solution(N, A, L)
