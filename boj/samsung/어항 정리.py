def print_board(board):
    for bo in board:
        print(bo)
    print()


def add_fish(board):
    fish_min = min(board[-1])
    for i in range(N):
        if board[-1][i] == fish_min:
            board[-1][i] += 1


# j번째 줄 왼쪽으로 한칸씩 밀기
def padding_left(board, j):
    for i in range(N - 1):
        board[j][i] = board[j][i + 1]
    board[j][N - 1] = 0


# 첫번째 공중 부양 어항 정리
def build_fishbowl(board):
    # 먼저 맨 왼쪽 어항 쌓기
    board[-2][0] = board[-1][0]

    # 90 도 회전
    def turn():
        nonlocal height
        nonlocal width
        nonlocal bowl_width
        temp = []
        # 회전 시킬 어항 길이 만큼 반복
        for i in range(bowl_width):
            line = []
            # 어항이 없을때까지 찾기
            for j in range(N - 1, -1, -1):
                if board[j][i] == 0:
                    break
                # 어항이 존재하면 해당 어항 line에 추가
                line.append(board[j][i])
            # temp 에 line 어항들 추가
            temp.append(line)
        # 회전시킨 어항 길이 만큼 left_padding
        for _ in range(bowl_width):
            padding_left(board, -1)

        # 회전시킨 어항의 개수만큼
        # 위에서 부터 채우면 90도 회전시킨 효과랑 동일
        n = len(temp)
        for i in range(n, 0, -1):
            for j in range(len(temp[n - i])):
                board[N - 1 - i][j] = temp[n - i][j]

        # 변수들 초기화
        width -= bowl_width
        height = len(temp) + 1
        bowl_width = len(temp[0])

    # 어항 높이
    height = 1
    # 맨 밑 어항의 길이
    width = N - 1
    # 90도 회전시킬 어항의 길이
    bowl_width = 1

    padding_left(board, -1)
    turn()

    # 못 쌓을때 까지 반복
    while height <= width - bowl_width:
        turn()


# 어항이동 함수
def control_fish(board):
    # 모든 어항이 동시에 이동하기 때문에 증감을 담아둘 변수 선언
    temp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                current = board[i][j]
                for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    new_i = i + direct[0]
                    new_j = j + direct[1]

                    # 격자를 안벗어나고 어항 물고기가 더큰 곳에서 작은곳으로만 이동하도록 조건
                    if 0 <= new_i < N and 0 <= new_j < N and board[new_i][new_j] > board[i][j]:
                        new = board[new_i][new_j]
                        d = (new - current) // 5
                        if d > 0:
                            temp[new_i][new_j] -= d
                            temp[i][j] += d

    # 기존 어항에 증감해주기
    for i in range(N):
        for j in range(N):
            board[i][j] += temp[i][j]


# 어항 일렬로 놓기
def spread_bowl(board):
    new_bowl = []
    # 가장 왼쪽 어항부터 , 아래에서 위쪽 어항 순으로 순서대로 놓아야함
    for j in range(N):
        for i in range(N):
            # 어항이 없으면 break
            if board[N - 1 - i][j] == 0:
                break
            new_bowl.append(board[N - 1 - i][j])

    # 맨 밑 어항을 제외한 어항 0으로 초기화
    for i in range(N - 1):
        board[i] = [0 for _ in range(N)]
    # 마지막 줄은 일렬로 놓은 어항
    board[-1] = new_bowl


# 두번째 공중부양 하기
def air_bowl(board):
    # 초기 어항 높이
    height = 1
    # 총 어항 길이
    width = N

    # 총 두번 반복
    for _ in range(2):
        temp = []
        # 어항 높이만큼 반복
        for i in range(height, 0, -1):
            _temp = []
            # 어항 길이의 / 2 만큼 잘라서 왼쪽 어항만 수행
            # a, b, c, d 일경우 b, a 순으로 채우고 그대로 쌓으면 180도 회전효과
            # b a
            # c d
            for j in range((width // 2) - 1, -1, -1):
                _temp.append(board[N - i][j])

            # 0 채우기
            for _ in range(N - len(_temp)):
                _temp.append(0)
            temp.append(_temp)

        # 감소하는 어항 개수만큼 패딩하기
        for idx in range(1, height + 1):
            for _ in range(width // 2):
                padding_left(board, -idx)

        # 어항 쌓기
        # 180 도 회전효과를 위해서
        # 가장 처음 temp 어항을 밑에서부터 쌓아야함
        for idx in range(1, height + 1):
            board[N - idx - height] = temp[idx - 1]

        # 어항 높이는 1 증가, 길이는 / 2
        width = width // 2
        height += 1


def solution(fishes):
    answer = 1
    board = [[0 for _ in range(N)] for _ in range(N)]
    board[-1] = fishes

    while True:
        add_fish(board)
        build_fishbowl(board)
        control_fish(board)
        spread_bowl(board)
        air_bowl(board)
        control_fish(board)
        spread_bowl(board)
        _max = max(board[-1])
        _min = min(board[-1])
        if _max - _min <= K:
            break
        answer += 1
    return answer


N, K = map(int, input().split())
fishes = list(map(int, input().split()))
print(solution(fishes))
