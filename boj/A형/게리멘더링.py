import collections
import itertools


# 해당 팀이 연결되어있는지 확인하기
# 확인 방법
# 현재 팀에 존재하지 않는 정점들은 FALSE, 팀에 존재하는 정점은 TRUE로 VISIT 초기화
# BFS 탐색시 팀에 존재하는 정점을 모두다 방문 할 수 있는지 검색하기
def connect(team, graph):
    start = team[0]
    visit = [False if v in team else True for v in range(N)]
    visit[start] = True
    Q = collections.deque()
    Q.append(start)
    n = len(team)
    count = 1

    while Q:
        v = Q.popleft()

        for adjacent in graph[v]:
            if not visit[adjacent]:
                visit[adjacent] = True
                Q.append(adjacent)
                count += 1
    return True if n == count else False


def solution(peoples, infos):
    answer = float('+inf')
    graph = collections.defaultdict(list)
    for idx in range(N):
        count = infos[idx][0]
        for i in range(1, 1 + count):
            graph[idx].append(infos[idx][i] - 1)
    vertex = [i for i in range(N)]

    # 지역 수는 최대 100개 -> 각 지역구 별로 최대 수는 N // 2개
    # 모든 경우를 조합으로 구하기
    for i in range(1, N // 2 + 1):
        combs = itertools.combinations(vertex, i)
        for comb in combs:
            team_2 = list(set(vertex) - set(comb))
            # 두 개의 지역구가 올바른 지역구인지 판단하기
            if connect(list(comb), graph) and connect(team_2, graph):
                A = 0
                B = 0
                # 각 지역구 인원수 구하기
                for idx in range(len(comb)):
                    A += peoples[comb[idx]]
                for idx in range(len(team_2)):
                    B += peoples[team_2[idx]]
                # 최소값으로 업데이트
                answer = min(answer, abs(A - B))
    if answer == float('+inf'):
        return -1
    return answer


N = int(input())
peoples = list(map(int, input().split()))
infos = [list(map(int, input().split())) for _ in range(N)]
print(solution(peoples, infos))
