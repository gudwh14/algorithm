import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


# R 연산
# 행 계산
def calc_R(A):
    max_len = 0
    for i in range(len(A)):
        counts = collections.Counter(A[i])
        # 0 은 카운팅 X
        if counts[0]:
            counts.pop(0)
        counts = list(map(list, counts.items()))
        counts.sort(key=lambda x: (x[1], x[0]))
        A[i] = sum(counts, [])
        # 크기가 100보다 크면 100자리 까지 자르기
        if len(A[i]) > 100:
            A[i] = A[i][:101]
        max_len = max(max_len, len(A[i]))

    pad_0(max_len, A)


# C 연산
# 열 계산
def calc_C(A):
    # A 의 배열의 각 열을 탐색하여 카운팅 후, 역배열로 구현
    new_A = []
    max_len = 0
    for j in range(len(A[0])):
        counts = collections.defaultdict(int)
        for i in range(len(A)):
            counts[A[i][j]] += 1
        # 0 은 카운팅 X
        # defaultdict인 경우, key를 참조했을때 값이 없는경우 기본값 0이 할당됨
        # 따라서 키를 한번 참조 해주고 해당키 삭제하기
        counts[0] = 1
        counts.pop(0)
        counts = list(map(list, counts.items()))
        counts.sort(key=lambda x: (x[1], x[0]))
        _count = sum(counts, [])
        # 크기가 100보다 크면 100자리 까지 자르기
        if len(_count) > 100:
            _count = _count[:101]
        max_len = max(max_len, len(_count))
        new_A.append(_count)
    pad_0(max_len, new_A)

    return new_A


def pad_0(max_len, A):
    # 최대 길이만큼 0 패딩해주기
    for i in range(len(A)):
        now_len = len(A[i])
        if now_len != max_len:
            for _ in range(max_len - now_len):
                A[i].append(0)


def solution(r, c, k, A):
    answer = 0
    is_right_state = True

    while True:
        # 100번이하로 풀수 없으면 -1
        if answer > 100:
            return - 1

        # 정배열일경우 A[r][c]
        if is_right_state:
            try:
                if A[r - 1][c - 1] == k:
                    break
            except IndexError:
                pass
        # 역배열일경우 A[c][r]
        else:
            try:
                if A[c - 1][r - 1] == k:
                    break
            except IndexError:
                pass

        # 행, 열 길이 구하기
        row = len(A)
        col = len(A[0])

        # 정배열일경우 기존과 그대로 로직 수행
        if is_right_state:
            if row >= col:
                calc_R(A)
            # C 연산 이후 역배열이 됨으로 is_right_state 토글 해주기
            else:
                A = calc_C(A)
                is_right_state = not is_right_state
        # 역배열일경우 행 개수 > 열 개수 일때면 R 연산 행 개수 <= 열 개수 이면 C 연산 이후 토글
        else:
            if row > col:
                calc_R(A)
            else:
                A = calc_C(A)
                is_right_state = not is_right_state

        answer += 1
    return answer


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
print(solution(r, c, k, A))
