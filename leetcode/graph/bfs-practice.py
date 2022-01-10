import collections

# bfs 는 재귀로 구현 할 수 없다
def bfs(start_v):
    discovered = [start_v]
    queue = collections.deque()
    queue.append(start_v)

    while queue:
        vertex = queue.popleft()
        for adjacent in graph[vertex]:
            if adjacent not in discovered:
                discovered.append(adjacent)
                queue.append(adjacent)

    return discovered


graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}

print(bfs(1))
