import collections
import heapq


# 다익스트라 알고리즘!
def solution(n, edge):
    answer = 0
    graph = collections.defaultdict(list)
    for v, u in edge:
        graph[v].append(u)
        graph[u].append(v)

    queue = []
    distances = collections.defaultdict(list)
    heapq.heappush(queue, (0, 1))

    while queue:
        current_distance, node = heapq.heappop(queue)

        if node not in distances:
            distances[node] = current_distance

            for adjacent_node in graph[node]:
                new_distance = current_distance + 1
                heapq.heappush(queue, (new_distance, adjacent_node))

    _max = max(distances.items(), key=lambda x: x[1])[1]
    for node, count in distances.items():
        if count == _max:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
