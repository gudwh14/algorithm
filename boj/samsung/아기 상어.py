import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()

# 초기 상어 위치와, 물고기들의 위치를 구하는 함수
def calc_location(N, board):
    shark = ()
    fish = []

    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                if board[i][j] == 9:
                    shark = (i, j)
                else:
                    fish.append((i, j, board[i][j]))

    return shark, fish


# 상어가 먹을수 있는 물고기들을 구하는 함수
def find_eat_fish(shark_size, fish):
    find = []
    for i, j, size in fish:
        if shark_size > size:
            find.append((i, j, size))

    return find


# 상어가 해당 물고기 칸으로 이동할 때 이동한 칸의 개수
def move_shark(N, board, shark_size, shark, dest):
    result = float('+inf')
    i, j = shark
    Q = collections.deque()
    Q.append((i, j, 0))
    directions = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    visit = [[False] * N for _ in range(N)]
    visit[i][j] = True

    while Q:
        ni, nj, distance = Q.popleft()
        if (ni, nj) == dest:
            result = min(result, distance)
            continue

        for direct in directions:
            next_i = ni + direct[0]
            next_j = nj + direct[1]

            if 0 <= next_i < N and 0 <= next_j < N and not visit[next_i][next_j]:
                if board[next_i][next_j] <= shark_size:
                    Q.append((next_i, next_j, distance + 1))
                    visit[next_i][next_j] = True
    return result


# 상어가 해당 물고기를 먹는 함수
def eat_fish(board, dest, fish):
    global shark_size, shark, eat_count
    board[shark[0]][shark[1]] = 0
    ti, tj, size = dest
    board[ti][tj] = 0
    shark = (ti, tj)

    eat_count += 1
    fish.remove(dest)
    if eat_count >= shark_size:
        eat_count = 0
        shark_size += 1


def solution(N, board):
    answer = 0
    global shark
    shark, fish = calc_location(N, board)

    while True:
        find = find_eat_fish(shark_size, fish)
        # 먹을수 있는 물고기가 없으면 종료
        if not find:
            break

        # 먹을수 있는 물고기가 1개이면 해당 물고기 먹으러가기
        if len(find) == 1:
            ti, tj = find[0][0], find[0][1]
            # 거리 구하기
            distance = move_shark(N, board, shark_size, shark, (ti, tj))
            # inf 이면 닿을수 없는 곳
            if distance == float('+inf'):
                break
            answer += distance
            eat_fish(board, find[0], fish)
        else:
            distances = []
            # 물고기들의 거리를 계산하여 저장
            for dest in find:
                ti, tj, size = dest[0], dest[1], dest[2]
                distance = move_shark(N, board, shark_size, shark, (ti, tj))
                distances.append([ti, tj, size, distance])

            # 거리가 짧은순, 좌표값 위쪽, 왼쪽 순으로 정렬
            distances.sort(key=lambda x: (x[3], x[0], x[1]))
            # 거리가 inf 이면 닿을수 없는곳
            if distances[0][3] == float('+inf'):
                break
            answer += distances[0][3]
            eat_fish(board, (distances[0][0], distances[0][1], distances[0][2]), fish)
    return answer


N = int(input().split()[0])
board = [list(map(int, input().split())) for _ in range(N)]

shark = None
shark_size = 2
eat_count = 0
print(solution(N, board))
