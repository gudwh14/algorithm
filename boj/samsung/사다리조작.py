import itertools
import sys


def print_board(board):
    for bo in board:
        print(bo)
    print()


# 사다리 게임 시작하는 함수
def start_game(n, board, hor_ladder):
    # 열을 조사
    for ladder in range(1, n + 1):
        i = 0
        j = ladder
        while board[i][j] != '끝':
            # 밑으로 내려가기
            i += 1
            # 수평 사다리 만나면 이동하기
            if hor_ladder[i][j]:
                j += 1
            elif hor_ladder[i][j - 1]:
                j -= 1
        # 일치하지 않으면 FALSE 반환 및 종료
        if j != ladder:
            return False
    return True


def solution(n, m, h, ladder):
    # 사다리 게임 보드 그리기
    board = [['ㅣ' for _ in range(n + 2)] for _ in range(h + 2)]
    hor_ladder = [[False] * (n + 2) for _ in range(h + 2)]

    for i, j in ladder:
        hor_ladder[i][j] = True

    for i in range(h + 2):
        for j in range(n + 2):
            if i == 0:
                board[i][j] = '시'
            if i == h + 1:
                board[i][j] = '끝'
            if j == 0 or j == n + 1:
                board[i][j] = '빈'

    # 수평 사다리를 설치할수 있는 유효한 좌표를 저장하는 변수
    ladders = []
    for i in range(1, h + 1):
        for j in range(1, n):
            # 현재 놓여진 수평사다리와 비교하여 동일한 사다리가 있는지, 설치하려는 사다리 좌우에 수평사다리가 있는지 바교
            if not hor_ladder[i][j] and not hor_ladder[i][j - 1] and not hor_ladder[i][j + 1]:
                ladders.append([i, j])

    # 0 ~ 3개까지 수평사다리를 설치할수있는 조합을 구하여 반복문 실행
    for count in range(0, 4):
        for comb in list(itertools.combinations(ladders, count)):
            flag = False
            _hor_ladder = [item[:] for item in hor_ladder]
            for ladder in comb:
                i, j = ladder
                # 추가할 수평사다리가 유요한 수평사다리인지 검사
                if hor_ladder[i][j - 1] or _hor_ladder[i][j + 1]:
                    flag = True
                    break

                _hor_ladder[i][j] = True
            if not flag:
                # 게임 성공하면 count 반환
                if start_game(n, board, _hor_ladder):
                    return count
    # 실패하면 -1
    return -1


n, m, h = map(int, input().split())
ladder = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

print(solution(n, m, h, ladder))
