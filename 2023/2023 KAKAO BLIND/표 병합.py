def solution(commands):
    answer = []
    board = [['EMPTY' for _ in range(51)] for _ in range(51)]
    idx = [[-1 for _ in range(51)] for _ in range(51)]
    # 병합 된 셀 key값, key가 같으면 병합된 셀
    cmd_idx = 0

    for command in commands:
        command = command.split(' ')

        if command[0] == 'UPDATE':
            if len(command) == 4:
                r, c, value = int(command[1]), int(command[2]), command[3]
                get_idx = idx[r][c]

                # 병합된 셀이 없을 경우
                if get_idx == -1:
                    board[r][c] = value
                    idx[r][c] = cmd_idx
                else:
                    for i in range(51):
                        for j in range(51):
                            if idx[i][j] == get_idx:
                                board[i][j] = value

            if len(command) == 3:
                value1 = command[1]
                value2 = command[2]

                for i in range(51):
                    for j in range(51):
                        if board[i][j] == value1:
                            board[i][j] = value2

        if command[0] == 'MERGE':
            r1, c1, r2, c2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])
            get_merge_id = idx[r1][c1]
            get_idx = idx[r2][c2]

            # (r1, c1), (r2 , c2) 중 셀값이 존재하는 value선택
            if board[r1][c1] == 'EMPTY':
                value = board[r2][c2]
            else:
                value = board[r1][c1]

            # (r1, c1)가 병합된 셀이 없을 경우
            if get_merge_id == -1:
                get_merge_id = cmd_idx
                idx[r1][c1] = cmd_idx

            # (r2, c2)가 병합된 셀이 없을 경우
            if get_idx == -1:
                idx[r2][c2] = get_merge_id
                board[r2][c2] = board[r1][c1]

            else:
                for i in range(51):
                    for j in range(51):
                        if idx[i][j] == get_idx:
                            idx[i][j] = get_merge_id
                for i in range(51):
                    for j in range(51):
                        if idx[i][j] == get_merge_id:
                            board[i][j] = value

        if command[0] == 'UNMERGE':
            r, c = int(command[1]), int(command[2])
            get_idx = idx[r][c]

            for i in range(51):
                for j in range(51):
                    if idx[i][j] == get_idx and not (r, c) == (i, j):
                        board[i][j] = 'EMPTY'
                        idx[i][j] = -1

        if command[0] == 'PRINT':
            r, c = int(command[1]), int(command[2])
            answer.append(board[r][c])
        cmd_idx += 1

    return answer