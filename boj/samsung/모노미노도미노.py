def print_board(board):
    for bo in board:
        print(bo)
    print()


# 초록색판에 블럭 설치
def build_green_block(block, board):
    # 설치할 블럭들
    blocks = []
    t, x, y, = block
    blocks.append((x, y))
    # 블럭 타입에 따른 블럭 추가
    if t == 2:
        blocks.append((x, y + 1))
    if t == 3:
        blocks.append((x + 1, y))

    # 만약 블럭 타입이 2 -> 가로 2 x 1 블럭이면
    if t == 2:
        # 해당 블럭을 설치할수 있는 높이 찾기
        r = float('+inf')
        for block in blocks:
            x, y = block
            idx = 0
            while idx <= 5:
                if board[idx][y] == 1:
                    break
                idx += 1

            r = min(r, idx - 1)
        # 해당 높이에 2 * 1 블럭 설치
        for block in blocks:
            board[r][block[1]] = 1
    # 블럭 타입 1, 3
    else:
        # 설치 할 수 있는 높이 찾기
        for block in blocks:
            x, y = block
            idx = 0
            while idx <= 5:
                if board[idx][y] == 1:
                    break
                idx += 1
            # 설치
            board[idx - 1][y] = 1


def check_green(green):
    # 터트릴수 있는 행 저장하는 변수
    find = []
    # 점수
    score = 0
    # 터트릴수 있는 행 찾기
    for i in range(2, 6):
        count = 0
        for j in range(4):
            if green[i][j] == 1:
                count += 1
        if count == 4:
            find.append(i)
            score += 1
    # 터트리기
    for idx in find:
        # 해당 행 터트리기
        for j in range(4):
            green[idx][j] = 0
        # 위에있는 블록 내리기
        for j in range(4):
            temp = None
            next_temp = None
            for i in range(idx):
                if temp == None:
                    next_temp = green[i + 1][j]
                    green[i + 1][j] = green[i][j]
                    temp = next_temp
                else:
                    next_temp = green[i + 1][j]
                    green[i + 1][j] = temp
                    temp = next_temp
    return score


# 밝은 칸에 있는 블록 찾기
def check_light_green(green):
    # 밝은 칸에 해당하는 행에 블럭이 얼마나 존재하는지 카운팅
    count = 0
    for i in range(2):
        for j in range(4):
            if green[i][j] == 1:
                count += 1
                break
        if count > 1:
            continue
    # 존재하는 행 만큼 반복
    for _ in range(count):
        # 마지막 행 블럭들 제거
        for j in range(4):
            green[5][j] = 0

        # 위에있는 블록 내리기
        for j in range(4):
            temp = 0
            next_temp = None
            # 주의 -1 부터 temp 0으로 시작하여 한칸씩 내려줘야함
            for i in range(-1, 5):
                if temp == None:
                    next_temp = green[i + 1][j]
                    green[i + 1][j] = green[i][j]
                    temp = next_temp
                else:
                    next_temp = green[i + 1][j]
                    green[i + 1][j] = temp
                    temp = next_temp


# 파란색은 초록색과 행,열 반대로 구현
def build_blue_block(block, board):
    blocks = []
    t, x, y, = block
    blocks.append((x, y))
    if t == 2:
        blocks.append((x, y + 1))
    if t == 3:
        blocks.append((x + 1, y))

    if t == 3:
        r = float('+inf')
        for block in blocks:
            x, y = block
            idx = 0
            while idx <= 5:
                if board[x][idx] == 1:
                    break
                idx += 1
            r = min(r, idx - 1)

        for block in blocks:
            board[block[0]][r] = 1
    else:
        for block in blocks:
            x, y = block
            idx = 0
            while idx <= 5:
                if board[x][idx] == 1:
                    break
                idx += 1

            board[x][idx - 1] = 1


def check_blue(blue):
    find = []
    score = 0
    # 터트릴수 있는 열 찾기
    for j in range(2, 6):
        count = 0
        for i in range(4):
            if blue[i][j] == 1:
                count += 1
        if count == 4:
            find.append(j)
            score += 1

    # 터트리기
    for idx in find:
        # 해당 열 터트리기
        for i in range(4):
            blue[i][idx] = 0
        # 위에있는 블록 내리기
        for i in range(4):
            temp = None
            next_temp = None
            for j in range(idx):
                if temp == None:
                    next_temp = blue[i][j + 1]
                    blue[i][j + 1] = blue[i][j]
                    temp = next_temp
                else:
                    next_temp = blue[i][j + 1]
                    blue[i][j + 1] = temp
                    temp = next_temp
    return score


def check_light_blue(blue):
    count = 0
    for j in range(2):
        for i in range(4):
            if blue[i][j] == 1:
                count += 1
                break
        if count > 1:
            continue

    for _ in range(count):
        # 마지막 열 터트리기
        for i in range(4):
            blue[i][5] = 0

        # 위에있는 블록 내리기
        for i in range(4):
            temp = 0
            next_temp = None
            for j in range(-1, 5):
                if temp == None:
                    next_temp = blue[i][j + 1]
                    blue[i][j + 1] = blue[i][j]
                    temp = next_temp
                else:
                    next_temp = blue[i][j + 1]
                    blue[i][j + 1] = temp
                    temp = next_temp


def calc_count(green, blue):
    count = 0
    for i in range(6):
        for j in range(4):
            if green[i][j] == 1:
                count += 1

    for i in range(4):
        for j in range(6):
            if blue[i][j] == 1:
                count += 1
    return count


def solution(N, blocks):
    answer = 0
    # 초록색 판 배열 생성
    green = [[0 for _ in range(4)] for _ in range(6)]
    # 파란색 판 배열 생성
    blue = [[0 for _ in range(6)] for _ in range(4)]

    for block in blocks:
        # 해당 블럭 쌓아 주기
        build_green_block(block, green)
        build_blue_block(block, blue)
        # 조건에 만족하는 블럭 터트리기
        answer += check_green(green)
        answer += check_blue(blue)
        # 밝은 칸에있는 블럭 탐색
        check_light_green(green)
        check_light_blue(blue)

    print(answer)
    print(calc_count(green, blue))


N = int(input())
blocks = [list(map(int, input().split())) for _ in range(N)]
solution(N, blocks)
