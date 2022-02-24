import collections

def print_board(board):
    for bo in board:
        print(bo)
    print()


# board 초기 설정 함수
# 바이러스 위치 좌표와, 빈칸의 개수를 반환함
def init_board(N, board):
    virus = []
    count = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                board[i][j] = '벽'
            elif board[i][j] == 2:
                virus.append([i, j])
                board[i][j] = '*'
            elif board[i][j] == 0:
                count += 1
                board[i][j] = float('+inf')

    return virus, count


# 조합을 만들어주는 함수
def combination(result: list, comb: list, start, depth, length):
    if depth == 0:
        result.append(comb[:])

    for i in range(start, length):
        comb.append(i)
        combination(result, comb, i + 1, depth - 1, length)
        comb.pop()


# 0: 빈칸 1: 벽 2: 비활성 바이러스 3: 활성 바이러스
def solution(N, M, board):
    answer = []
    virus, empty_count = init_board(N, board)
    combs = []
    combination(combs, [], 0, M, len(virus))
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for idx, comb in enumerate(combs):
        # 깊은 복사
        _board = [item[:] for item in board]

        # BFS 탐색
        Q = collections.deque()
        visit = [[False] * N for _ in range(N)]
        # M 개 바이러스를 활성바이러스로 변경
        for active_idx in comb:
            r, c = virus[active_idx]
            _board[r][c] = 0
            visit[r][c] = True
            Q.append((r, c, 0))

        count = 0
        result = 0
        while Q:
            if count == empty_count:
                break
            i, j, time = Q.popleft()
            # 해당 칸이 빈칸이면 time 값 부여, 카운트 증가
            if _board[i][j] == float('+inf'):
                _board[i][j] = time
                count += 1
            # 해당칸이 비활성 바이러스이면 바이러스에 time만 부여
            elif _board[i][j] == '*':
                _board[i][j] = time

            # 총 걸리는 시간
            result = max(result, _board[i][j])

            # 상, 하, 좌, 우 탐색
            for direct in directions:
                ni = i + direct[0]
                nj = j + direct[1]

                # 인덱스가 올바르고 해당칸이 벽이 아니면 탐색
                if 0 <= ni < N and 0 <= nj < N and not visit[ni][nj] and _board[ni][nj] != '벽':
                    Q.append((ni, nj, time + 1))
                    visit[ni][nj] = True

        # 바이러스로 변한 빈공간의 개수가, 총 빈공간의 개수랑 같지 않으면
        # 바이러스가 퍼질수 없는곳
        if count != empty_count:
            result = float('+inf')
        answer.append(result)

    answer.sort()
    # 바이러스가 퍼질수 없으면 -1 리턴
    if answer[0] == float('+inf'):
        return -1
    return answer[0]


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
