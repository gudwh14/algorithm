# 수직검사 함수
def find_path_vertical(n, l, i, j, board):
    # 이전값을 저장하는 변수
    prev = board[i][j]
    # 경사로를 만들었는지 판단하는 변수
    runway = False
    # 경사로의 길이를 저장하는 변수
    count = 0
    # 경사로가 설치된 자표를 저장하는 변수
    visit = []

    for x in range(n):
        # print((i + x, j), prev, board[i + x][j], runway, count, visit)

        # 이전값과 현재값을 비교
        # 같을경우 이동할수있는 길
        if prev == board[i + x][j]:
            # 경사로가 설치되어있으면, 경사로를 늘려서 설치
            if runway:
                visit.append((i + x, j))
                count += 1
            # 이전값 업데이트
            prev = board[i + x][j]
        # 같지 않으면
        else:
            # 경사로가 미설치 상태일때
            if not runway:
                # 이전값과 현재값 값비교
                # 1 일경우 하강하는 경사로 설치
                if prev - board[i + x][j] == 1:
                    # 이미 해당 좌표에 경사로가 있으면 실패!
                    if (i + x, j) in visit:
                        return False
                    runway = True
                    count += 1
                    prev = board[i + x][j]
                    visit.append((i + x, j))
                # -1 일경우 상승하는 경사로 설치
                elif prev - board[i + x][j] == -1:
                    down_count = 0
                    # 길이가 l인 경사로가 만들어지는 판단
                    for idx in range(i + x - 1, -1, -1):
                        # 이미 해당 좌표에 경사로가 있으면 실패!
                        if (idx, j) in visit:
                            return False
                        if prev == board[idx][j]:
                            down_count += 1
                            visit.append((idx, j))
                        else:
                            return False
                        if down_count == l:
                            break
                    # l 보다 작은 경사로가 만들어지면 이동 할 수 없는 길
                    if down_count < l:
                        return False
                    prev = board[i + x][j]
                # 높이 차이가 1보다 클경우 이동 할 수 없는 길!
                else:
                    return False
            # 값이 같지않은데 경사로가 설치 되어있으면 맨처음 높이값과 1보다 차이가 크게 난다는 뜻 -> 이동 할수 없는 길
            elif runway:
                return False

        # 경사로의 길이가 l 만큼 경사로가 만들어지면
        # 경사로 만들기 종료
        if count == l:
            prev = board[i + x][j]
            count = 0
            runway = False

    # 경사로가 남아있고 경사로의 길이가 l 보다 작으면 이동 할 수 없는 길
    if runway and count < l:
        return False
    # print(i, j, visit)
    return True


def find_path_horizon(n, l, i, j, board):
    prev = board[i][j]
    runway = False
    count = 0
    visit = []

    for y in range(n):
        # print((i, j + y), prev, board[i][j + y], runway, count)

        if prev == board[i][j + y]:
            if runway:
                visit.append((i, j + y))
                count += 1
            prev = board[i][j + y]
        else:
            if not runway:
                if prev - board[i][j + y] == 1:
                    if (i, j + y) in visit:
                        return False
                    runway = True
                    count += 1
                    prev = board[i][j + y]
                    visit.append((i, j + y))
                elif prev - board[i][j + y] == -1:
                    down_count = 0
                    for idx in range(j + y - 1, -1, -1):
                        if (i, idx) in visit:
                            return False
                        if prev == board[i][idx]:
                            down_count += 1
                            visit.append((i, idx))
                        else:
                            return False
                        if down_count == l:
                            break
                    if down_count < l:
                        return False
                    prev = board[i][j + y]
                else:
                    return False
            elif runway:
                return False

        if count == l:
            prev = board[i][j + y]
            count = 0
            runway = False

    if runway and count < l:
        return False
    # print(i, j, visit)
    return True


def solution(n, l, board):
    answer = 0

    # 행, 열의 시작점 좌표만 체크
    for i in range(n):
        for j in range(n):
            # 수직 검사
            if i == 0:
                # (0, 0) 일경우 수직, 수평 다 검사
                if j == 0:
                    if find_path_horizon(n, l, i, j, board):
                        answer += 1
                if find_path_vertical(n, l, i, j, board):
                    answer += 1
            # 수평 검사
            else:
                if j == 0:
                    if find_path_horizon(n, l, i, j, board):
                        answer += 1

    return answer


n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, l, board))
