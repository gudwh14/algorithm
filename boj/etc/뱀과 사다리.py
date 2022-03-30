import collections


def solution(N, M, ladders, snakes):
    answer = float('+inf')
    ladder = {}
    snake = {}
    for x, y in ladders:
        ladder[x] = y

    for x, y in snakes:
        snake[x] = y

    visit = [[False, float('+inf')] for _ in range(101)]
    Q = collections.deque()
    Q.append((1, 0))
    visit[1] = [True, 0]

    while Q:
        now, count = Q.popleft()

        if now == 100:
            answer = min(answer, count)

        for dice in range(1, 7):
            new_x = now + dice

            if new_x in ladder:
                new_x = ladder[new_x]

            if new_x in snake:
                new_x = snake[new_x]
            if new_x > 100:
                continue
            if not visit[new_x][0] or (visit[new_x][0] == True and visit[new_x][1] > count + 1):
                Q.append((new_x, count + 1))
                visit[new_x] = [True, count + 1]

    return answer


N, M = map(int, input().split())
ladders = [list(map(int, input().split())) for _ in range(N)]
snakes = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, ladders, snakes))
