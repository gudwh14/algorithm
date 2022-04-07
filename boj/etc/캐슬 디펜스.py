import itertools


def find_shot_enemy(N, enemy, archer, D):
    temp = []
    a_r = N
    a_c = archer
    for r, c in enemy:
        distance = abs(a_r - r) + abs(a_c - c)
        if distance <= D:
            temp.append((r, c, distance))

    temp.sort(key=lambda x: (x[2], x[1]))
    if temp:
        return (temp[0][0], temp[0][1])
    return temp


def solution(N, M, D, board):
    answer = 0
    archers_comb = list(itertools.combinations([n for n in range(M)], 3))
    enemies = []

    for i in range(N - 1, -1, -1):
        for j in range(M):
            if board[i][j] == 1:
                enemies.append((i, j))

    for archers in archers_comb:
        count = 0
        enemy = enemies[:]
        while True:
            shots = set()

            for archer in archers:
                shot = find_shot_enemy(N, enemy, archer, D)
                if shot:
                    shots.add(shot)
            for shot in shots:
                enemy.remove(shot)
                count += 1
            new_enemy = []
            for i in range(len(enemy)):
                new_i = enemy[i][0] + 1
                if new_i == N:
                    continue
                new_enemy.append((new_i, enemy[i][1]))

            enemy = new_enemy[:]
            if not enemy:
                break
        answer = max(count, answer)
    return answer


N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, D, board))
