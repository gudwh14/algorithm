import itertools


def print_board(board):
    for bo in board:
        print(bo)
    print()

# 배열 회전 시키는 함수
# 배열 회전시 이러한 방식이 아닌 뒤에서 한칸씩 밀면 로직을 더 간단하게 구현 가능!

def turn(A, r, c, s):
    if s == 0:
        return
    start = (r - s, c - s)
    end = (r + s, c + s)

    # 오른쪽으로 밀기
    temp = None
    for j in range(start[1], end[1]):
        if temp == None:
            temp = A[start[0]][j]
            _temp = A[start[0]][j + 1]
            A[start[0]][j + 1] = temp
            temp = _temp
        else:
            _temp = A[start[0]][j + 1]
            A[start[0]][j + 1] = temp
            temp = _temp

    # 아래쪽으로 밀기
    for i in range(start[0], end[0]):
        _temp = A[i + 1][end[1]]
        A[i + 1][end[1]] = temp
        temp = _temp

    # 왼쪽으로 밀기
    for j in range(end[1], start[1], -1):
        _temp = A[end[0]][j - 1]
        A[end[0]][j - 1] = temp
        temp = _temp

    # 위쪽으로 밀기
    for i in range(end[0], start[0], -1):
        _temp = A[i - 1][start[1]]
        A[i - 1][start[1]] = temp
        temp = _temp

    # 더이상 회전 할 수 없을 때까지 재귀
    turn(A, r, c, s - 1)


# 각행의 sum 값중 최솟값 구하기
def calc(A):
    min_value = float('+inf')
    for i in range(N):
        min_value = min(min_value, sum(A[i]))

    return min_value


def solution(A, infos):
    answer = float('+inf')
    perms = list(itertools.permutations(infos))

    for perm in perms:
        _A = [item[:] for item in A]
        for r, c, s in perm:
            turn(_A, r - 1, c - 1, s)
        answer = min(answer, calc(_A))

    return answer


N, M, K = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
infos = [list(map(int, input().split())) for _ in range(K)]
print(solution(A, infos))
