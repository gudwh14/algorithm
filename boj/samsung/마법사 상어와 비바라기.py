def move_cloud(N, cloud, direction, s):
    directions = [(), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
    r, c = cloud
    new_r = (r + directions[direction][0] * s) % N
    new_c = (c + directions[direction][1] * s) % N
    # -1 -> 4, -2 -> 3, -3 -> 2, -4, 1  -5, 0 -6 -> 1
    if new_r < 0:
        new_r += N

    if new_c < 0:
        new_c += N

    return (new_r, new_c)


def count_water(N, cloud, board):
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
    r, c = cloud

    for direct in directions:
        new_r = r + direct[0]
        new_c = c + direct[1]

        if 0 <= new_r < N and 0 <= new_c < N and board[new_r][new_c] > 0:
            board[r][c] += 1


def create_new_cloud(N, board, new_clouds):
    clouds = []
    for i in range(N):
        for j in range(N):
            # 물이 2이상인 칸과 과정 3 에서 구름이 사라진 칸이 아니면 새로운 구름 생성
            if board[i][j] >= 2 and (i, j) not in new_clouds:
                clouds.append((i, j))
                board[i][j] -= 2
    return clouds


def solution(N, M, board, infos):
    # 초기 구름 위치
    clouds = [(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)]

    # M번 이동하기
    for i in range(M):
        # 구름 이동방향, 이동속도
        directions, s = infos[i]

        new_clouds = []
        # 구름 이동하여 새로운 좌표 얻기
        for cloud in clouds:
            new_clouds.append(move_cloud(N, cloud, directions, s))

        # 구름이 존재하는 칸에 물 +1
        for cloud in new_clouds:
            r, c = cloud
            board[r][c] += 1

        # 물복사 버그 시전
        for cloud in new_clouds:
            count_water(N, cloud, board)

        clouds = create_new_cloud(N, board, new_clouds)

    answer = 0
    for i in range(N):
        for j in range(N):
            answer += board[i][j]
    return answer


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
infos = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, board, infos))
