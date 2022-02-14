import sys


def init(n, board):
    for i in range(n + 2):
        for j in range(n + 2):
            if i == 0 or i == n + 1 or j == 0 or j == n + 1:
                board[i][j] = '#'

    board[1][1] = '머'


def solution(n, apples, turns):
    answer = 1
    # 오, 왼, 위, 아래 방향 으로 전진할때 좌표 값 증감
    directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    # 초기 머리 방향
    heading = 0
    # 처음 머리 좌표
    head = [1, 1]
    # 꼬리 좌표
    tail = None
    board = [['_' for _ in range(n + 2)] for _ in range(n + 2)]
    init(n, board)
    visit = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    while True:
        # 방향에 따른 x,y 좌표 증감값 가져오기
        x, y = directions[heading]

        # 전진 로직
        if tail:
            # 꼬리가 있으면 몸길이가 늘어남
            board[head[0]][head[1]] = '몸'
        else:
            # 최초 꼬리가 없을때, 꼬리 만들어주기
            board[head[0]][head[1]] = '꼬'
        # 머리가 있는 좌표에 대한 방향값을 저장함 -> 나중 꼬리가 해당 위치에 있으면 해당 방향으로 이동
        visit[head[0]][head[1]] = heading
        # 머리 전진
        head[0] += x
        head[1] += y
        # 전진 했을경우 벽을 만나거나 꼬리를 만나거나 몸통을 만나면 종료
        if board[head[0]][head[1]] == '#' or board[head[0]][head[1]] == '꼬' or board[head[0]][head[1]] == '몸':
            break

        # 진행할경우, 머리 한칸 이동
        board[head[0]][head[1]] = '머'

        # 사과를 먹는 로직
        # 해당 좌표에 사과가 있으면 처리
        if (head[0], head[1]) in apples:
            # 꼬리가 없을시
            if not tail:
                # 꼬리 좌표 만들어주기
                tail = [head[0] - x, head[1] - y]
            # 먹은 사과 제거
            apples.remove((head[0], head[1]))
        # 사과가 없으면 해당 방향으로 한칸 전진
        else:
            # 꼬리가 있을시
            if tail:
                # 원래 꼬리 좌표를
                board[tail[0]][tail[1]] = '_'
                # 꼬리가 움직이는 방향 가져오기
                tail_x, tail_y = directions[visit[tail[0]][tail[1]]]
                # 꼬리 좌표 이동
                tail[0] += tail_x
                tail[1] += tail_y
                # 꼬리 이동
                board[tail[0]][tail[1]] = '꼬'
            # 꼬리가 없으면 전진하여 생긴 꼬리 제거
            else:
                board[head[0] - x][head[1] - y] = '_'

        # 방향 전환 로직
        for times, dir in turns:
            if int(times) == answer:
                if dir == 'D':
                    if heading == 0:
                        heading = 3
                    elif heading == 1:
                        heading = 2
                    elif heading == 2:
                        heading = 0
                    elif heading == 3:
                        heading = 1
                elif dir == 'L':
                    if heading == 0:
                        heading = 2
                    elif heading == 1:
                        heading = 3
                    elif heading == 2:
                        heading = 1
                    elif heading == 3:
                        heading = 0
                # 해당 좌표에 변한 방향값 업데이트
                visit[head[0]][head[1]] = heading
        answer += 1
    return answer


n = int(sys.stdin.readline())
n_apple = int(sys.stdin.readline())
apples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n_apple)]
n_turns = int(sys.stdin.readline())
turns = [tuple(map(str, sys.stdin.readline().split())) for _ in range(n_turns)]
print(solution(n, apples, turns))
