import collections


# BFS + DP 를 이용한 풀이
def solution(board):
    n = len(board)
    # 초기값은 최대값 설정
    answer = float('+inf')
    dp = [[float('+inf') for _ in range(n)] for _ in range(n)]
    # 현재 지나간 길을 확인하기(방향을 확인하기) 위해 idx 추가
    # (i , j, idx)
    directions = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]
    # i, j, cost, directions
    q = collections.deque([(0, 0, 0, -1)])

    while q:
        i, j, cost, dir_idx = q.popleft()
        print(i, j, cost, dir_idx)
        # i, j 가 우측 맨하단에 도착하고 (도착지점), 현재 cost 가 더작으면 값 할당
        if (i, j) == (n - 1, n - 1) and answer > cost:
            answer = cost

        for direction in directions:
            # 다음 방향으로 좌표 이동
            next_i = i + direction[0]
            next_j = j + direction[1]
            # 현재 방향과, 다음 방향이 같으면 직진으로 판단, 맨 처음 시작지점이면 상관없이 직진으로 판단
            if dir_idx == direction[2] or dir_idx == -1:
                add_cost = 100
            # 코너 비용 500 + 직선비용 100
            else:
                add_cost = 600

            # 벽을 만나거나 , i, j 인덱스 값이 유효하지 않으면 스킵
            if not (0 <= next_i < n and 0 <= next_j < n) or board[next_i][next_j] == 1:
                continue
            # 이미 방문한 좌표 일경우 최소 비용이 아니면 스킵
            # Ex) 이전에 방문한 비용이 직진 비용이고, 이번 방분이 코너 방문이면 스킵
            if dp[next_i][next_j] < cost + add_cost - 400:
                continue

            # dp에 값 설정 및 큐 추가
            dp[next_i][next_j] = cost + add_cost
            q.append((next_i, next_j, cost + add_cost, direction[2]))

    return answer


print(solution([[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0],
                [1, 0, 0, 0, 0, 0, 0, 0]]))
