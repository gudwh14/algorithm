def solution(n, computers):
    answer = 0
    visit = []

    def dfs(computer, index):
        visit.append(index)

        for i in range(n):
            if i not in visit and computer[i] == 1:
                dfs(computers[i], i)

    while len(visit) != n:
        for i in range(n):
            if i not in visit:
                dfs(computers[i], i)
                answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
print(solution(1, [[1]]))
