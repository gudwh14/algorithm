import sys

def solution(n, m, board):
    answer = []

    # 회전, 대칭시켜 나올수 있는 모든 테트로미노를 모든 좌표마다 한개씩 놓아 최대값 구하기!
    # 총 19개의 모형이 나온다
    for i in range(n):
        for j in range(m):
            try:
                answer.append(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i][j + 3])  # case1
            except IndexError:
                pass

            try:
                answer.append(board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 3][j])  # case2
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1])  # case3
            except IndexError:
                pass

            try:
                answer.append(board[i][j] + board[i + 1][j] + board[i + 2][j] + board[i + 2][j + 1])  # case4
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j])  # case5
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j + 1])  # case6
            except IndexError:
                pass
            try:
                answer.append(board[i][j + 2] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])  # case7
            except IndexError:
                pass
            try:
                answer.append(board[i][j + 1] + board[i + 1][j + 1] + board[i + 2][j] + board[i + 2][j + 1])  # case8
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 2])  # case9
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i][j + 1] + board[i + 1][j] + board[i + 2][j])  # case10
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])  # case11
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1])  # case12
            except IndexError:
                pass
            try:
                answer.append(board[i][j + 1] + board[i][j + 2] + board[i + 1][j] + board[i + 1][j + 1])  # case13
            except IndexError:
                pass
            try:
                answer.append(board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j])  # case14
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i][j + 1] + board[i + 1][j + 1] + board[i + 1][j + 2])  # case15
            except IndexError:
                pass
            try:
                answer.append(board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 1][j + 2])  # case16
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j])  # case17
            except IndexError:
                pass
            try:
                answer.append(board[i][j] + board[i][j + 1] + board[i][j + 2] + board[i + 1][j + 1])  # case18
            except IndexError:
                pass
            try:
                answer.append(board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1] + board[i + 2][j + 1])  # case19
            except IndexError:
                pass

    # 오름차순 정렬
    answer.sort()
    # 최대값 리턴
    return answer[-1]


n, m = list(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, m, board))
