import collections


def solution(m, n, board):
    answer = 0
    queue = collections.deque()
    # board 를 배열리스트로 전환
    boards = []
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(board[i][j])
        boards.append(temp)
    board = boards

    # 지울수있는 블럭 찾기 큐에 시작 좌표 저장
    def find():
        for i in range(0, m - 1):
            for j in range(0, n - 1):
                if 'A' <= board[i][j] <= 'Z' and board[i][j] == board[i + 1][j] == board[i][j + 1] == board[i + 1][
                    j + 1]:
                    queue.append([i, j])

    # 반복
    while True:
        # 지울수있는 블럭 찾기
        find()
        # 지울수 있는 블럭이 없으면 종료
        if not queue:
            break
        # 지울수 있는 블럭이 있으면 해당 블럭 지우기
        while queue:
            i, j = queue.popleft()
            board[i][j] = "펑"
            board[i + 1][j] = "펑"
            board[i][j + 1] = "펑"
            board[i + 1][j + 1] = "펑"
        # 지워진 블럭 제거하고 블럭 내리기
        # 블럭을 내릴때 밑에서 부터 검색하여 '펑', '빈' 을 찾으면 가장 가까운 블럭이랑 교체하기
        for i in range(m - 1, 0, -1):
            for j in range(n):
                if board[i][j] == '펑' or board[i][j] == '빈':
                    idx = -1
                    for k in range(i, -1, -1):
                        if 'A' <= board[k][j] <= 'Z':
                            idx = k
                            break
                    if idx != -1:
                        board[i][j] = board[idx][j]
                        board[idx][j] = '빈'

    # 제거한 블럭이 몇개인지 카운팅
    for i in range(m):
        for j in range(n):
            if board[i][j] == '빈' or board[i][j] == '펑':
                answer += 1

    return answer


print(solution(6, 2, ["DD", "CC", "AA", "AA", "CC", "DD"]))
print(solution(8, 2, ["FF", "AA", "CC", "AA", "AA", "CC", "DD", "FF"]))
print(solution(6, 2, ["AA", "AA", "CC", "AA", "AA", "DD"]))
