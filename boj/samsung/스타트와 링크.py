
# 능력치 구하는 함수
def calc_stat(team, S):
    stats = 0

    # S[i][j] 에 해당하는 값을 다 더해준다
    for i in team:
        for j in team:
            stats += S[i][j]

    return stats


def solution(n, S):
    answer = []
    people = [i for i in range(n)]
    start_team = []
    link_team = []

    # comb 로 start_team 구하기
    def dfs(ele, start, depth):
        if depth == n / 2:
            start_team.append(ele[:])

        for i in range(start, n):
            ele.append(i)
            dfs(ele, i + 1, depth + 1)
            ele.pop()

    dfs([], 0, 0)

    # start_team을 바탕으로 link_team 구하기
    for team in start_team:
        ele = []
        for p in people:
            if p not in team:
                ele.append(p)

        link_team.append(ele)

    # 두팀간의 능력치 차이를 answer에 저장
    for idx in range(len(start_team)):
        answer.append(abs(calc_stat(start_team[idx], S) - calc_stat(link_team[idx], S)))

    # 오름차순으로 정렬
    answer.sort()
    # 가장 능력치 차이가 작은 값을 반환
    return answer[0]


n = int(input().split()[0])
S = [list(map(int, input().split())) for _ in range(n)]

print(solution(n, S))
