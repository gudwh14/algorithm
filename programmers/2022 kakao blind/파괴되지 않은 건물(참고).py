def solution(board, skill):
    answer = 0
    acc = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]

    # 모든 스킬에 대해서 누적합 구하기
    for sk in skill:
        type = sk[0]
        if type == 1:
            degree = -sk[5]
        elif type == 2:
            degree = sk[5]

        acc[sk[1]][sk[2]] += degree
        acc[sk[1]][sk[4] + 1] += -degree
        acc[sk[3] + 1][sk[2]] += -degree
        acc[sk[3] + 1][sk[4] + 1] += degree

    # 위에서 아래로 누적합 더하기
    for j in range(len(acc[0])):
        for i in range(len(acc) - 1):
            acc[i + 1][j] += acc[i][j]

    # 왼쪽에서 오른쪽으로 누적합 더하기
    for i in range(len(acc)):
        for j in range(len(acc[0]) - 1):
            acc[i][j + 1] += acc[i][j]

    # 기존 board 에 누적합을 구한 배열 더해서 파괴되지 않은 건물 개수 구하기
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += acc[i][j]
            if board[i][j] > 0:
                answer += 1

    return answer


# print(solution([[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]],
#                [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]]))
print(solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]))
