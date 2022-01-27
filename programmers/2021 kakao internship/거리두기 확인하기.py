import collections


# BFS 로 탐색하여 확인해야함
def bfs(place, i, j):
    queue = collections.deque()
    # 방향을 나타냄
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    # 방문한 곳인지 확인하는 배열
    visit = [[False] * 5 for _ in range(5)]
    # 거리를 확인하는 카운팅
    count = 0
    # 초기 값 설정
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()
        # 해당 좌표 방문 처리
        visit[i][j] = True

        # 방향으로 이동
        for direction in directions:
            ni = i + direction[0]
            nj = j + direction[1]

            # 올바른 인덱스인지 판단 아닐경우 스킵
            if ni < 0 or ni >= 5 or nj < 0 or nj >= 5:
                continue
            # 이미 방문한 좌표이면 스킵
            if visit[ni][nj]:
                continue
            # 벽을 만나면 스킵
            if place[ni][nj] == 'X':
                continue
            # 사람을 만나면 return BFS 탐색 종료
            if place[ni][nj] == 'P':
                return False
            # 거리 1내에 가림막('O') 만났을경우 해당칸을 한번더 검사 해야함으로 큐에 넣어준다
            queue.append((ni, nj))

        count += 1
        # 처음 응시자(시작점) 기준으로 2바퀴를 돌았을 때는 맨하튼 거리 2를 넘어가게 되므로
        # 이 때까지 False를 리턴하지 않았다면 거리두기를 잘 지킨 것이므로 True를 리턴해준다
        if count == 2:
            return True
    return True


def solution(places):
    answer = []
    n = 5

    for place in places:
        flag = True
        for i in range(n):
            for j in range(n):
                if place[i][j] == 'P':
                    if not bfs(place, i, j):
                        flag = False
                        break

        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
