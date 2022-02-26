def print_board(board):
    for bo in board:
        print(bo)
    print()


def move_mal(N, K, mals, mals_location, board):
    directions = [(), (0, 1), (0, -1), (-1, 0), (1, 0)]

    for idx in range(1, K + 1):
        r, c, direct = mals_location[idx]
        mal_list = mals[r][c]

        # 해당칸에 말이 1개일경우
        if len(mal_list) == 1:
            next_r = r + directions[direct][0]
            next_c = c + directions[direct][1]

            # 이동하려는 칸이 파란색이거나 체스판을 벗어날 경우
            if not (0 <= next_r < N) or not (0 <= next_c < N) or board[next_r][next_c] == 2:
                # 방향 바꾸기
                if direct == 1:
                    new_direct = 2
                elif direct == 2:
                    new_direct = 1
                elif direct == 3:
                    new_direct = 4
                elif direct == 4:
                    new_direct = 3

                new_r = r + directions[new_direct][0]
                new_c = c + directions[new_direct][1]

                # 새롭게 이동하려는 칸이 체스판을 벗어나거나 파란색일경우 이동하지 않는다.
                if not (0 <= new_r < N) or not (0 <= new_c < N) or board[new_r][new_c] == 2:
                    mals_location[idx] = [r, c, new_direct]
                # 아니경우
                else:
                    if board[new_r][new_c] == 0:
                        mals[new_r][new_c].extend(mal_list)
                        mals[r][c].clear()
                        mals_location[idx] = [new_r, new_c, new_direct]
                    elif board[new_r][new_c] == 1:
                        mals[new_r][new_c].extend(mal_list)
                        mals[r][c].clear()
                        mals_location[idx] = [new_r, new_c, new_direct]
            # 이동하려는 칸이 흰색
            elif board[next_r][next_c] == 0:
                mals[next_r][next_c].extend(mal_list)
                mals[r][c].clear()
                mals_location[idx] = [next_r, next_c, direct]
            # 이동하려는 칸이 빨간색
            elif board[next_r][next_c] == 1:
                mals[next_r][next_c].extend(mal_list)
                mals[r][c].clear()
                mals_location[idx] = [next_r, next_c, direct]
        # 해당칸에 다른말들이 존자하면
        elif len(mal_list) > 1:
            # 내가 업은말인지 업힌 말인지 판단
            mal_index = mal_list.index(idx)
            next_r = r + directions[direct][0]
            next_c = c + directions[direct][1]

            if not (0 <= next_r < N) or not (0 <= next_c < N) or board[next_r][next_c] == 2:
                # 방향 바꾸기
                if direct == 1:
                    new_direct = 2
                elif direct == 2:
                    new_direct = 1
                elif direct == 3:
                    new_direct = 4
                elif direct == 4:
                    new_direct = 3

                new_r = r + directions[new_direct][0]
                new_c = c + directions[new_direct][1]
                # 새롭게 이동하려는 칸이 체스판을 벗어나거나 파란색일경우 이동하지 않는다.
                if not (0 <= new_r < N) or not (0 <= new_c < N) or board[new_r][new_c] == 2:
                    for mal_number in mal_list[mal_index:]:
                        if mal_number == idx:
                            mals_location[mal_number] = [r, c, new_direct]
                        else:
                            _direct = mals_location[mal_number][2]
                            mals_location[mal_number] = [r, c, _direct]
                # 아니경우
                else:
                    if board[new_r][new_c] == 0:
                        mals[new_r][new_c].extend(mal_list[mal_index:])
                        for mal_number in mal_list[mal_index:]:
                            if mal_number == idx:
                                mals_location[mal_number] = [new_r, new_c, new_direct]
                            else:
                                _direct = mals_location[mal_number][2]
                                mals_location[mal_number] = [new_r, new_c, _direct]
                        mals[r][c] = mals[r][c][:mal_index]

                    # 이동하려는 칸이 빨간색
                    elif board[new_r][new_c] == 1:
                        mal_list = mal_list[mal_index:]
                        mal_list.reverse()
                        mals[new_r][new_c].extend(mal_list)
                        for mal_number in mal_list:
                            if mal_number == idx:
                                mals_location[mal_number] = [new_r, new_c, new_direct]
                            else:
                                _direct = mals_location[mal_number][2]
                                mals_location[mal_number] = [new_r, new_c, _direct]
                        mals[r][c] = mals[r][c][:mal_index]
            # 이동하려는 칸이 흰색
            elif board[next_r][next_c] == 0:
                mals[next_r][next_c].extend(mal_list[mal_index:])
                for mal_number in mal_list[mal_index:]:
                    if mal_number == idx:
                        mals_location[mal_number] = [next_r, next_c, direct]
                    else:
                        _direct = mals_location[mal_number][2]
                        mals_location[mal_number] = [next_r, next_c, _direct]

                mals[r][c] = mals[r][c][:mal_index]

            # 이동하려는 칸이 빨간색
            elif board[next_r][next_c] == 1:
                mal_list = mal_list[mal_index:]
                mal_list.reverse()
                mals[next_r][next_c].extend(mal_list)
                for mal_number in mal_list:
                    if mal_number == idx:
                        mals_location[mal_number] = [next_r, next_c, direct]
                    else:
                        _direct = mals_location[mal_number][2]
                        mals_location[mal_number] = [next_r, next_c, _direct]
                mals[r][c] = mals[r][c][:mal_index]

        if check_4(K, mals, mals_location):
            return True


def check_4(K, mals, mals_location):
    for idx in range(1, K + 1):
        r, c, direct = mals_location[idx]
        if len(mals[r][c]) >= 4:
            return True
    return False


def solution(N, K, board, mals, mals_locations):
    answer = 1
    while True:
        if answer > 1000:
            return -1
        if move_mal(N, K, mals, mals_locations, board):
            break

        answer += 1

    return answer


N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
mals = [[[] for _ in range(N)] for _ in range(N)]
mals_location = [[] for _ in range(K + 1)]
for i in range(1, K + 1):
    r, c, direct = map(int, input().split())
    mals[r - 1][c - 1].append(i)
    mals_location[i] = [r - 1, c - 1, direct]

print(solution(N, K, board, mals, mals_location))
