def solution(board, moves):
    answer = 0
    # 크레인 크기
    n = len(board)
    # 인형을 담을 바구니
    baguni = []

    # 크레인 이동
    for move in moves:
        # 해당칸 위에서부터 0이 아닌 값 찾기
        for i in range(n):
            if board[i][move - 1] != 0:
                # 바구니에 해당 인형 담기
                baguni.append(board[i][move - 1])
                # 해당인형 칸에서 제거
                board[i][move - 1] = 0
                # 한개를 뽑으면 탈출
                break

        # 같은 종류 인형 2개가 쌓이면 제거
        while len(baguni) >= 2 and baguni[-1] == baguni[-2]:
            baguni.pop()
            baguni.pop()
            answer += 2

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
