import collections
import copy


def solution(info, edges):
    answer = 0
    graph = collections.defaultdict(list)
    # 방문 가능한 정점 배열, 초기 값은 0번 노드로 설정
    path = [0]
    # 양의 수, 늑대의 수
    sheep, wolf = 0, 0

    # 단방향 그래프 만들기
    for u, v in edges:
        graph[u].append(v)

    def dfs(vertex, path, sheep, wolf):
        # 깊은 복사로, 배열 복사 해오기
        _path = copy.deepcopy(path)
        # 방문한 정점을, 방문 가능한 정점배열에서 삭제 해주기
        _path.remove(vertex)

        # 양, 늑대 체크
        if info[vertex] == 0:
            sheep += 1
        elif info[vertex] == 1:
            wolf += 1

        # 결과를 저장 하는 변수
        nonlocal answer
        # 양의 최대값으로 할당
        answer = max(answer, sheep)

        # 만약 양의 수가 늑대수보다 많으면, 방문 가능한 노드에 인접한 노드들 넣어주기
        if sheep > wolf:
            for adjacent in graph[vertex]:
                _path.append(adjacent)
        # 늑대수가 양의 수랑 같거나 많으면 종료
        else:
            return

        # 방문가능한 노드 방문!
        for v in _path:
            dfs(v, _path, sheep, wolf)

    dfs(0, path, sheep, wolf)
    return answer


print(solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
               [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]))
