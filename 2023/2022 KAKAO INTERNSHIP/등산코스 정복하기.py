import collections


def solution(n, paths, gates, summits):
    answer = []
    graph = collections.defaultdict(list)
    gate_info = [False] * (n + 1)
    summit_info = [False] * (n + 1)
    distance = [float('+inf')] * (n + 1)

    for gate in gates:
        gate_info[gate] = True

    for summit in summits:
        summit_info[summit] = True

    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    for gate in gates:
        Q = collections.deque()
        Q.append((gate, 0))

        while Q:
            node, intensity = Q.popleft()

            if summit_info[node]:
                continue

            for adjacent, weight in graph[node]:
                if not gate_info[adjacent]:
                    new_intensity = max(intensity, weight)

                    if new_intensity < distance[adjacent]:
                        Q.append((adjacent, new_intensity))
                        distance[adjacent] = new_intensity

    for summit in summits:
        answer.append((summit, distance[summit]))
    answer.sort(key=lambda x: (x[1], x[0]))
    return answer[0]