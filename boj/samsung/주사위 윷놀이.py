import collections


# def move_mal(mal, dice):
#     i, j = mal
#     if i == 1:
#         if j + dice > 7:
#             new_i = 5
#             new_j = 0
#         elif j + dice > 3:
#             new_i = 4
#             new_j = (j + dice) % 4
#         else:
#             new_i = i
#             new_j = j + dice
#     elif i == 2:
#         if j + dice > 6:
#             new_i = 5
#             new_j = 0
#         elif j + dice > 2:
#             new_i = 4
#             new_j = (j + dice) % 3
#         else:
#             new_i = i
#             new_j = j + dice
#     elif i == 3:
#         if j + dice > 7:
#             new_i = 5
#             new_j = 0
#         elif j + dice > 3:
#             new_i = 4
#             new_j = (j + dice) % 4
#         else:
#             new_i = i
#             new_j = j + dice
#     elif i == 0:
#         if j + dice > 19:
#             new_i = 5
#             new_j = 0
#         elif j + dice == 19:
#             new_i = 4
#             new_j = 3
#         else:
#             new_i = i
#             new_j = j + dice
#     elif i == 4:
#         if j + dice > 3:
#             new_i = 5
#             new_j = 0
#         else:
#             new_i = i
#             new_j = j + dice
#
#     if new_i == 0:
#         if new_j == 4:
#             new_i = 1
#             new_j = 0
#         elif new_j == 9:
#             new_i = 2
#             new_j = 0
#         elif new_j == 14:
#             new_i = 3
#             new_j = 0
#
#     if new_i == 4:
#         if new_j > 3:
#             new_i = 5
#             new_j = 0
#
#     return new_i, new_j
#
#
# def solution(dice):
#     answer = []
#     test = []
#     mal = [(0, -1), (0, -1), (0, -1), (0, -1)]
#     map = [[2, 4, 6, 8, 0, 12, 14, 16, 18, 0, 22, 24, 26, 28, 0, 32, 34, 36, 38],
#            [10, 13, 16, 19],
#            [20, 22, 24],
#            [30, 28, 27, 26],
#            [25, 30, 35, 40],
#            [0]]
#
#     i, j = move_mal(mal[0], dice[0])
#     mal[0] = (i, j)
#     total = map[i][j]
#     Q = collections.deque()
#     Q.append((mal, total, 0))
#
#     while Q:
#         mal, total, turn = Q.popleft()
#         # 주사위 10번을 다쓰면 종료
#         if turn == 9:
#             answer.append(total)
#             test.append(mal)
#             continue
#
#         # 4개 말 이동하는 경우의 수
#         for idx in range(4):
#             # 해당 말이 도착이 아니면 움직일수있음
#             if mal[idx] != (5, 0):
#                 # 말배열 복사
#                 _mal = mal[:]
#                 # 해당 말이 새롭게 이동하는 좌표
#                 new_i, new_j = move_mal(_mal[idx], dice[turn + 1])
#                 # 해당 좌표가 도착지점이면 무조건이동가능
#                 # 해당 좌표에 다른말이 있으면 이동 불가
#                 if (new_i, new_j) == (5, 0) or (new_i, new_j) not in _mal:
#                     # 해당 말 좌표 이동
#                     _mal[idx] = (new_i, new_j)
#                     # 점수 추가
#                     _total = total + map[new_i][new_j]
#                     # 다음 주사위 굴리기
#                     Q.append((_mal, _total, turn + 1))
#                 else:
#                     continue
#     answer.sort()
#     return answer[-1]
#
#
# dice = list(map(int, input().split()))
# print(solution(dice))


def go(cnt, rlt):
    global ans
    if cnt == 10:
        ans = max(ans, rlt)
        return
    for i in range(4):
        graph, pos = H[i]
        nxt_graph, nxt_pos = graph, pos + D[cnt]
        if graph == -1:
            continue
        if graph == 4 and len(G[graph]) <= nxt_pos:
            nxt_graph, nxt_pos = -1, -1
        elif graph == 0 and len(G[graph]) + 1 <= nxt_pos:
            nxt_graph, nxt_pos = -1, -1
        elif graph in [1, 2, 3] and pos == len(G[graph]) - 1 and D[cnt] == 5:
            nxt_graph, nxt_pos = -1, -1
        else:
            if graph == 0 and (nxt_pos in [5, 10, 15, 20]):
                if nxt_pos == 5:
                    nxt_graph = 1
                    nxt_pos = 0
                elif nxt_pos == 10:
                    nxt_graph = 2
                    nxt_pos = 0
                elif nxt_pos == 15:
                    nxt_graph = 3
                    nxt_pos = 0
                else:
                    nxt_graph = 4
                    nxt_pos = 3
            elif graph in [1, 2, 3] and len(G[graph]) <= nxt_pos:
                nxt_graph, nxt_pos = 4, nxt_pos - len(G[graph])
            if [nxt_graph, nxt_pos] in H:
                continue
        H[i] = [nxt_graph, nxt_pos]
        if nxt_graph == -1:
            go(cnt + 1, rlt)
        else:
            go(cnt + 1, rlt + G[nxt_graph][nxt_pos])
        H[i] = [graph, pos]


D = list(map(int, input().split()))
H = [[0, 0]] * 4
G1 = [i for i in range(0, 40, 2)]
G2 = [10, 13, 16, 19]
G3 = [20, 22, 24]
G4 = [30, 28, 27, 26]
G5 = [25, 30, 35, 40]
G = [G1, G2, G3, G4, G5]
ans = 0
go(0, 0)
print(ans)
