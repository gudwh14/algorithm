def print_board(board):
    for bo in board:
        print(bo)

    print()


# 집에 해당하는 좌표들을 반환하는 함수
def find_house(n, board):
    house = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                house.append([i, j])

    return house

# 치킨집에 해당하는 좌표들을 반환하는 함수
def find_chicken(n, board):
    chickens = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 2:
                chickens.append([i, j])

    return chickens


# 조합을 만들어주는 함수
def combination(result: list, comb: list, start, depth, length):
    if depth == 0:
        result.append(comb[:])

    for i in range(start, length):
        comb.append(i)
        combination(result, comb, i + 1, depth - 1, length)
        comb.pop()


# 거리를 계산해주는 함수
# 로직) 집 좌표값, 치킨집 좌표값들을 이용하여 두점 사이의 거리중 최솟값을 저장하여 총 거리를 반환
def calc_distance(house, chickens):
    result = 0
    for h in house:
        distance = float('+inf')
        for chicken in chickens:
            distance = min(distance, abs(h[0] - chicken[0]) + abs(h[1] - chicken[1]))
        result += distance

    return result


def solution(n, m, board):
    answer = []
    house = find_house(n, board)
    chickens = find_chicken(n, board)

    for i in range(1, m + 1):
        # 조합을 이용하여, 치킨집을 1 ~ 3개까지 뽑는다.
        combinations = []
        combination(combinations, [], 0, i, len(chickens))

        # 각각의 조합을 바탕으로 치킨집 좌표값을 저장하여 거리를 계산
        for comb in combinations:
            _chickens = []
            for element in comb:
                _chickens.append(chickens[element])
            answer.append(calc_distance(house, _chickens))

    # 오름차순 정렬
    answer.sort()
    # 최솟값 반환
    return answer[0]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, m, board))
