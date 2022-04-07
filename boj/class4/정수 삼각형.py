def solution(n, tri):
    for i in range(1, n):
        for j in range(len(tri[i])):
            if j == 0:
                tri[i][j] = tri[i][j] + tri[i - 1][j]
            elif j == len(tri[i]) - 1:
                tri[i][j] = tri[i][j] + tri[i - 1][j - 1]
            else:
                tri[i][j] = tri[i][j] + max(tri[i - 1][j], tri[i - 1][j - 1])

    return max(tri[n - 1])


n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, tri))
