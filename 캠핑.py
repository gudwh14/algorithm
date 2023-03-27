import collections


def solution(grid, k):
    answer = float('+inf')
    n = len(grid)
    m = len(grid[0])
    visit = [[[False for _ in range(m)] for _ in range(n)] for _ in range(k + 1)]
    Q = collections.deque()
    Q.append((0, 0, 0, k))
    visit[k][0][0] = True

    while Q:
        r, c, count, remain = Q.popleft()

        # 이동할 수 있는 칸 횟수가 없으면 야영
        if remain == 0 and grid[r][c] == '.' and not visit[k][r][c]:
            Q.append((r, c, count + 1, k))
            visit[k][r][c] = True
            continue

        if not remain:
            continue

        # 각 칸마다 야영하기
        if not visit[k][r][c]:
            Q.append((r, c, count + 1, k))
            visit[k][r][c] = True

        for direct in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_r = r + direct[0]
            new_c = c + direct[1]
            if 0 <= new_r < n and 0 <= new_c < m and grid[new_r][new_c] != '#':
                # 목적지 도착
                if new_r == n - 1 and new_c == m - 1:
                    answer = min(answer, count)
                    continue

                if not visit[remain][new_r][new_c]:
                    Q.append((new_r, new_c, count, remain - 1))
                    visit[remain - 1][new_r][new_c] = True

    return answer


print(solution(grid=
               ["..FF", "###F", "###."], k=4))
print(solution(
    [".F.FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.",
     ".#...####F", "...#......"], 6))
print(solution(
    [".F#FFFFF.F", ".########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.",
     ".#...####F", "...#......"], 6))
print(solution(
    [".F.FFFFF.F", "#########.", ".########F", "...######F", "##.######F", "...######F", ".########F", ".########.",
     ".#...####F", "...#......"], 6))
