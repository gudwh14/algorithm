import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


# 가장큰 블럭 그룹 찾기
def find_group(N, board):
    rainbows = []

    def bfs(i, j):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        group = []
        group.append((i, j))
        Q = collections.deque()
        Q.append((i, j))
        visit[i][j] = True
        rain_bow = 0

        while Q:
            r, c = Q.popleft()

            for direct in directions:
                nr = r + direct[0]
                nc = c + direct[1]

                # 해당 좌표의 블럭이 같은 색의 블럭이거나 무지개색 블럭이면 그룹에 포함
                if 0 <= nr < N and 0 <= nc < N and (board[nr][nc] == board[i][j] or board[nr][nc] == 0) and not \
                        visit[nr][nc]:
                    Q.append((nr, nc))
                    group.append((nr, nc))
                    visit[nr][nc] = True
                    # 무지개색 블럭 개수 카운팅
                    if board[nr][nc] == 0:
                        rainbows.append((nr, nc))
                        rain_bow += 1
        # 그룹에 해당하는 블럭이 2개 이상일때만 그룹 인정
        if len(group) > 1:
            groups.append([i, j, len(group), rain_bow, group])

    visit = [[False for _ in range(N)] for _ in range(N)]
    groups = []
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and board[i][j] > 0:
                bfs(i, j)
                # 무지개색 블럭 방문 배열 초기화
                # 공통으로 사용 할 수 있기 때문에
                for r, c in rainbows:
                    visit[r][c] = False

    # 그룹의 블럭 개수, 무지개색 블럭 개수, 행, 열 순으로 정렬
    groups.sort(key=lambda x: (x[2], x[3], x[0], x[1]))
    return groups[-1]


# 중력작용 함수
def down_board(N, board):
    for j in range(N):
        for i in range(N - 1, 0, -1):
            # 해당 칸이 빈칸일경우, 그 칸 위부터 조사해서 내기기
            if board[i][j] == -2:
                for find_i in range(i - 1, -1, -1):
                    # 내릴수 없는 블럭이면 종료
                    if board[find_i][j] == -1:
                        break
                    # 내릴수 있는 블럭이면 위치 바꾸기
                    elif board[find_i][j] >= 0:
                        board[i][j] = board[find_i][j]
                        board[find_i][j] = -2
                        break


# 90 반시계 방향으로 회전 함수
def turn_board(N, board):
    new_board = [[-3 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[N - (1 + j)][i] = board[i][j]

    return new_board


def solution(N, M, board):
    answer = 0

    while True:
        # 가장큰 블록 그룹찾기
        try:
            find = find_group(N, board)
        # 그룹이 없으면 종료
        except IndexError:
            break
        i, j, count, rain_bow, group = find

        # 점수 획득
        answer += count ** 2
        # 블럭 지우기
        for r, c in group:
            board[r][c] = -2
        # 중력
        down_board(N, board)
        # 블럭 회전
        board = turn_board(N, board)
        # 중력
        down_board(N, board)

    return answer


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
