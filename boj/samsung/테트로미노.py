import sys
import collections

# 구현 로직
# BFS 를 사용하여 상, 하, 좌, 우에 대해서 가장 큰값으로 방문하여 탐색하면 테트로미노를 만족하는 4개의 블록을 탐색할수있다.
# 이때 ㅏ , ㅗ, ㅓ, ㅜ 에 해당하는 테트로미노에 대해서는 탐색이 안된다 -> 조건 추가
# 두번째 부터 방문한 좌표에 대해서 상, 하, 좌, 우에 해당하는 좌표에대한 값이, 이전에 방문했던 두번째 맥스값보다 작으면
# 현재 좌표의 최대값으로 방문하는것이 아니라 이전에 방문했던 두번째 맥스값의 좌표로 방문
def solution(n, m, board):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    answer = []

    # 모든 좌표에서 BFS 탐색
    for i in range(n):
        for j in range(m):
            Q = collections.deque()
            # 좌표마다 방문 배열 초기화
            visit = []
            # Q에 초기 좌표 초기화 하기 (i, j, 값, 카운트)
            Q.append((i, j, board[i][j], 1))
            # 바로 이전의 두번째 최대값을 가지는 변수 (i, j, 값)
            prev_second_max_value = ()

            while Q:
                ni, nj, nsum, count = Q.popleft()
                # visit 배열에 넣어주기
                visit.append((ni, nj))
                # 4개를 찾으면 종료 후 답 넣어주기
                if count == 4:
                    answer.append(nsum)
                    break

                # 이동할수있는 상, 하, 좌, 우 에 해당하는 (방향, 해당값)을 temp에 저장
                temp = []
                for idx, direct in enumerate(directions):
                    if 0 <= ni + direct[0] < n and 0 <= nj + direct[1] < m and (ni + direct[0], nj + direct[1]) not in visit:
                        temp.append([idx, board[ni + direct[0]][nj + direct[1]]])

                # 내림차순으로 정렬
                temp.sort(key= lambda  x: x[1], reverse=True)

                # temp 의 길이가 1보다 크면
                if len(temp) > 1:
                    # 두번째 큰 값에 대한 좌표를 구해놓기
                    prev_i = ni + directions[temp[1][0]][0]
                    prev_j = nj + directions[temp[1][0]][1]

                # 이전에 대한 두번째 큰 값이 존재한다면
                if prev_second_max_value:
                    # 현재 최대값이 이전에 대한 두번째 큰값 보다 크거나 같을때
                    if temp[0][1] >= prev_second_max_value[2]:
                        # 해당 좌표로 이동
                        ni += directions[temp[0][0]][0]
                        nj += directions[temp[0][0]][1]
                        Q.append((ni, nj, nsum + board[ni][nj], count + 1))
                    # 작으면
                    else:
                        # 이전에 대한 두번째 큰값으로 이동하기
                        Q.append((prev_second_max_value[0], prev_second_max_value[1], nsum + prev_second_max_value[2], count + 1))
                # 존재 X
                else:
                    # 최대값으로 좌표 이동
                    ni += directions[temp[0][0]][0]
                    nj += directions[temp[0][0]][1]
                    Q.append((ni, nj, nsum + board[ni][nj], count + 1))

                # temp 의 길이가 1보다 크면, 이전 값에 대한 두번째 큰값 설정해주기
                if len(temp) > 1:
                    prev_second_max_value = (prev_i, prev_j, temp[1][1])

    # 오름차순 정렬
    answer.sort()
    # 최대값 리턴
    return answer[-1]


n, m = list(map(int, sys.stdin.readline().split()))
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

print(solution(n, m, board))
