import collections


def print_board(board):
    for bo in board:
        print(bo)
    print()


# 국경선이 열리는 국가 좌표 구하는 함수
def calc_open(N, L, R, board):
    opens = []
    # visit 배열은 항상 o(1) 참조할수있도록 in 으로 탐색하는것이 아니라 False,True 로 참조하여 탐색하여야함
    visit = [[False] * N for _ in range(N)]
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for i in range(N):
        for j in range(N):
            # 방문하지 않은 국가일때 방문
            if not visit[i][j]:
                result = set()
                Q = collections.deque()
                Q.append((i, j))
                visit[i][j] = True

                while Q:
                    ni, nj = Q.popleft()

                    # 상, 하, 좌, 우 탐색
                    for direct in directions:
                        next_i = ni + direct[0]
                        next_j = nj + direct[1]
                        # 올바른 인덱스이고, 방문할 국가가 visit-> False 이면 조건 만족
                        if 0 <= next_i < N and 0 <= next_j < N and not visit[next_i][next_j]:
                            # 인구차이 조건을 만족해야함
                            if L <= abs(board[ni][nj] - board[next_i][next_j]) <= R:
                                # result에 국가 추가하기
                                result.add((ni, nj))
                                result.add((next_i, next_j))
                                Q.append((next_i, next_j))
                                visit[next_i][next_j] = True
                if result:
                    opens.append(list(result))
    return opens


# 국경선이 열린 나라들간 인구이동 함수
def move_people(union, board):
    n = len(union)
    total = 0
    for uni in union:
        total += board[uni[0]][uni[1]]

    for uni in union:
        board[uni[0]][uni[1]] = total // n


def solution(N, L, R, board):
    answer = 0
    while True:
        opens = calc_open(N, L, R, board)
        if not opens:
            break
        for union in opens:
            move_people(union, board)
        answer += 1

    return answer


N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, L, R, board))
