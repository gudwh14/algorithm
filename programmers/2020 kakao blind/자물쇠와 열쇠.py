# 열쇠 배열 90도 돌리기
def rotate90(key):
    n = len(key)
    # 회전한 배열을 저장할 배열
    ret = [[0] * n for _ in range(n)]

    # 배열 반복해서 회전 시키기
    for i in range(n):
        for j in range(n):
            # 규칙이 있음 (90도 회전하는 경우)
            # 1. 회전 후 배열의 X 인덱스 == 회전하기 전 배열의 Y 인덱스
            # 2. 회전 후 배열의 Y 인덱스 == (배열 크기 - 1) - 회전하기 전 배열의 X 인덱스
            ret[j][n - 1 - i] = key[i][j]
    return ret


# 열쇠가 자물쇠에 일치하는지 확인 하는 함수
def check(start_x, start_y, key, lock, expand_size, start, end):
    expand_list = [[0] * expand_size for _ in range(expand_size)]

    # expand_list 에 key 배열 넣기
    for i in range(len(key)):
        for j in range(len(key)):
            expand_list[start_x + i][start_y + j] += key[i][j]

    # expand_list 에 lock 배열 넣기 항상 중심에 넣어야함
    for i in range(start, end):
        for j in range(start, end):
            expand_list[i][j] += lock[i - start][j - start]
            # expand_list 에서 자물쇠 배열의 합이 1이 아니면 열쇠가 맞는 것이 아니다!
            if expand_list[i][j] != 1:
                return False
    return True


def solution(key, lock):
    start = len(key) - 1  # expandList에서 자물쇠의 시작 지점
    end = start + len(lock)  # expandList에서 자물쇠의 끝나는 지점
    # expandList 에 자물쇠는 항상 배열 중심에 존재함!
    expand_size = len(lock) + start * 2  # expandList 배열의 크기

    # expandList 배열에서 자물쇠는 중심에 고정되어있고, 키가 움직이면서 체크 해야함
    # 총 3번 회전 반복
    for _ in range(4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, expand_size, start, end):
                    return True
        key = rotate90(key)

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
