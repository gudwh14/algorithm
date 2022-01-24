import collections


def solution(tickets):
    answer = []
    graph = collections.defaultdict(list)

    # 티켓을 정렬하여 그래프로 저장
    for a, b in sorted(tickets):
        graph[a].append(b)

    def dfs(airport):
        while graph[airport]:
            # 정렬된 그래프에서 어휘순으로 방문해야 함으로 첫 번째 원소 부터 방문
            # 중복 방문을 막기위해서 pop 하여 원소 제거
            dfs(graph[airport].pop(0))
        # 방문한 공항 추가하기
        answer.append(airport)

    dfs('ICN')
    # 역순으로 방문 공항이 만들어짐으로 역순하여 리턴
    return answer[::-1]


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))