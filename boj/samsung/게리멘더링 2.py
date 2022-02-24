def print_board(board):
    for bo in board:
        print(bo)
    print()


# 유효한 d1, d2 값 리스트들을 반환해주는 함수
def calc_d1_d2(N, i, j):
    dlist = []
    for d1 in range(1, N):
        for d2 in range(1, N):
            # 문제에 주어진 조건 만족하기
            if i < i + d1 + d2 <= N - 1 and 0 <= j - d1 < j < j + d2 <= N - 1:
                dlist.append((d1, d2))

    return dlist


# 지역구 만들기
def make_area(N, d, i, j, A):
    # 각 지역구별 인원수
    a1, a2, a3, a4, a5 = 0, 0, 0, 0, 0
    d1, d2 = d

    # 경계선 배열
    boundary = [[0] * N for _ in range(N)]
    # 각 행마다 경계선에서 왼쪽 값을 저장하는 변수
    left = {}
    # 각 행마다 경계선에서 오른쪽 값을 저장하는 변수
    right = {}
    boundary[i][j] = 1
    # 경계선 구하기
    for idx in range(1, d1 + 1):
        boundary[i + idx][j - idx] = 1
        left[i + idx] = (j - idx)
        boundary[i + d2 + idx][j + d2 - idx] = 1
        right[i + d2 + idx] = (j + d2 - idx)
    for idx in range(1, d2 + 1):
        boundary[i + idx][j + idx] = 1
        right[i + idx] = (j + idx)
        boundary[i + d1 + idx][j - d1 + idx] = 1
        left[i + d1 + idx] = (j - d1 + idx)

    # 경계선에서 높이 는 d1 + d2
    height = d1 + d2
    # 높이에 해당하는 행을 구해서 경계선 안쪽을 5번 지역구로 만들어주기
    for r in range(i + 1, i + height):
        left_j = left[r]
        right_j = right[r]
        for c in range(left_j, right_j):
            boundary[r][c] = 1

    for r in range(N):
        for c in range(N):
            # 해당 지역이 경계선 지역이면 5번 지역구
            if boundary[r][c] == 1:
                a5 += A[r][c]
            # 나머지는 각 문제 조건에 맞는 지역구 해당
            elif 0 <= r < i + d1 and 0 <= c <= j:
                a1 += A[r][c]
            elif 0 <= r <= i + d2 and j < c <= N - 1:
                a2 += A[r][c]
            elif i + d1 <= r <= N - 1 and 0 <= c < j - d1 + d2:
                a3 += A[r][c]
            elif i + d2 < r <= N - 1 and j - d1 + d2 <= c <= N - 1:
                a4 += A[r][c]

    area = []
    area.append(a1)
    area.append(a2)
    area.append(a3)
    area.append(a4)
    area.append(a5)
    # 오름차순 정렬
    area.sort()
    # 가장 인원 많은 지역구 - 적은 인원 지역구 리턴
    return area[-1] - area[0]


def solution(N, A):
    answer = float('+inf')

    for i in range(N - 2):
        for j in range(1, N - 1):
            dlist = calc_d1_d2(N, i, j)

            for d in dlist:
                # 최소값 저장하기
                answer = min(answer, make_area(N, d, i, j, A))

    return answer


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, A))
